<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>✅ To Do List</title>
  <script src="https://cdn.jsdelivr.net/pyodide/v0.23.4/full/pyodide.js"></script>
  <style>
    /* Full-screen terminal aesthetic; cursor hidden to emphasize keyboard-driven interaction */
    html, body { height:100%; margin:0; cursor:none; }
    body {
      background:#000; color:#fff; font-family:"Courier New",monospace;
      font-size:0.9em; overflow:hidden;
    }

    /* Column layout: header, scrollable output, fixed input line */
    #terminal {
      display:flex; flex-direction:column; height:100%;
      padding:14px 20px 20px 20px; box-sizing:border-box; background:#000;
    }

    /* Header mirrors a Python REPL banner; left-aligned for authenticity */
    #header { margin-bottom:1em; white-space:pre-wrap; text-align:left; }

    /* Output hides native scrollbars for immersion; bottom spacer prevents overlap with input */
    #output {
      flex:1 1 auto; white-space:pre-wrap; overflow-y:auto;
      scrollbar-width:none; padding-bottom:12px;
    }
    #output::-webkit-scrollbar { display:none; }
    #output::after { content:""; display:block; height:64px; }

    /* Prompt + editable command area; custom block cursor added when ready */
    #input-line {
      flex:0 0 auto; display:inline-flex; align-items:center;
      margin-top:8px; padding-top:4px; line-height:1em;
    }
    #prompt, #command {
      font-family:"Courier New", monospace; font-size:0.9em; line-height:1em;
      display:inline-flex; align-items:center;
    }
    #prompt { margin-right:6px; }
    #command {
      outline:none; white-space:pre; caret-color:transparent;
      min-width:1ch; flex:1 1 auto;
    }
    /* Zero-width space prevents the empty contenteditable from collapsing */
    #command:empty::before { content:"\200B"; visibility:hidden; }
    /* Block cursor mimics terminal feel more faithfully than a text caret */
    #command.ready::after {
      content:""; display:inline-block; width:8px; height:1em;
      background:#fff; animation:blink 1s steps(1) infinite; margin-left:0;
    }
    @keyframes blink { 50% { background:transparent; } }
  </style>
</head>
<body>
  <div id="terminal">
    <div id="header"></div>
    <div id="output">
Welcome to To Do List

Options:

1. Add Task

2. Remove Task

3. Quit

Enter Your Choice, 1, 2, or 3
    </div>
    <div id="input-line">
      <span id="prompt">>>> </span>
      <span id="command" contenteditable="true"></span>
    </div>
  </div>

  <script type="text/python" id="py-code">
todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added")

def remove_task():
    if todo_list:
        removed = todo_list.pop()
        print(f"Task '{removed}' removed")
    else:
        print("Your To Do List is empty")
  </script>

  <script>
    const cmdEl=document.getElementById("command"), outEl=document.getElementById("output");

    // Auto-sticks to bottom unless the user scrolls up; threshold avoids jitter near the end
    let autoStick=true;
    function appendAndStick(txt){
      outEl.textContent+=txt;
      if(autoStick) outEl.scrollTop=outEl.scrollHeight;
    }
    outEl.addEventListener("scroll",()=>{
      autoStick=Math.abs(outEl.scrollHeight-outEl.scrollTop-outEl.clientHeight)<4;
    });

    // Input hygiene: remove invisible characters and normalize whitespace so commands parse reliably
    function sanitize(raw){
      return raw.replace(/[\u200B\u200C\u200D]/g,"")
                .replace(/\u00A0/g," ")
                .replace(/\r?\n/g,"")
                .trim();
    }

    // Pyodide boot: load runtime, then preload the Python functions to avoid first-command latency
    let pyodide;
    async function initPyodide(){
      pyodide=await loadPyodide();
      await pyodide.runPythonAsync(document.getElementById("py-code").textContent);
      cmdEl.classList.add("ready");
      cmdEl.focus();
    }

    // Capture Python stdout to keep UI output consistent with terminal expectations
    async function pyRunAndCapture(code){
      let buf=""; pyodide.setStdout({batched:s=>buf+=s});
      await pyodide.runPythonAsync(code);
      pyodide.setStdout({batched:()=>{}});
      return buf;
    }

    // Keep menu text reusable to restore state after clearing the list
    const MENU_TEXT=`\n\nOptions:\n\n1. Add Task\n\n2. Remove Task\n\n3. Quit\n\nEnter Your Choice, 1, 2, or 3`;
    let awaitingTask=false;
    // Single-source keywords prevent accidental fallthrough and make intent explicit
    const specials=new Set(["1","2","3","help","credits","license","copyright"]);

    // Command router: echo input, branch to menu actions, or request task text
    async function processCommand(raw){
      const original=sanitize(raw), low=original.toLowerCase();
      appendAndStick(`\n>>> ${original}\n\n`);
      if(!low) return;

      if(specials.has(low)){
        awaitingTask=false;
        if(low==="1"){ appendAndStick("Enter task"); awaitingTask=true; return; }
        if(low==="2"){ appendAndStick(await pyRunAndCapture("remove_task()")); return; }
        if(low==="3"){ await pyodide.runPythonAsync("todo_list.clear()"); appendAndStick("Your To Do List is empty"+MENU_TEXT); return; }
        if(low==="help"){ appendAndStick("Type the number of an option to execute it.\n\n1 = Add a task\n2 = Remove the last task\n3 = Quit the program"); return; }
        if(low==="credits"){ appendAndStick("This was originally created on Mimo."); return; }
        if(low==="license"){ appendAndStick("Python is distributed under the PSF License.\nSee https://docs.python.org/3/license.html for details."); return; }
        if(low==="copyright"){ appendAndStick("Copyright (c) 2001-2025 Python Software Foundation.\nAll Rights Reserved."); return; }
      }
      if(awaitingTask){
        appendAndStick(await pyRunAndCapture(`add_task(${JSON.stringify(original)})`));
        awaitingTask=false;
        return;
      }
      appendAndStick("Input not recognized, please type a valid input");
    }

    // Enter submits commands; clearing content keeps the input line visually stable
    cmdEl.addEventListener("keydown",async e=>{
      if(e.key==="Enter"){
        e.preventDefault();
        const raw=cmdEl.innerText;
        cmdEl.textContent="";
        await processCommand(raw);
      }
    });

    // REPL banner time-stamped to feel alive without distracting updates
    function formatDate(){
      const n=new Date();
      return `${n.toDateString()} ${String(n.getHours()).padStart(2,"0")}:${String(n.getMinutes()).padStart(2,"0")}`;
    }
    function updateHeader(){
      document.getElementById("header").textContent=
        `Python 3.15.0 (main, ${formatDate()}) [Clang 14.0.0]\nType "help", "credits", "license", "copyright"\nfor more information.`;
    }
    updateHeader(); setInterval(updateHeader,1000);

    // Cursor appears briefly on movement to signal focus, then hides to maintain terminal immersion
    let cursorTimer=null;
    window.addEventListener("mousemove",()=>{
      document.body.style.cursor="default";
      clearTimeout(cursorTimer);
      cursorTimer=setTimeout(()=>{ document.body.style.cursor="none"; },1200);
    });

    // Initialize after load to avoid race conditions with DOM readiness
    window.addEventListener("load",()=>{ initPyodide(); });
  </script>
</body>
</html>

