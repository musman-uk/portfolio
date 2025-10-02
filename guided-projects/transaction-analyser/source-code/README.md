```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>📊 Transaction Analyser</title>
  <script src="https://cdn.jsdelivr.net/pyodide/v0.23.4/full/pyodide.js"></script>
  <style>
    /* Full-screen terminal look; cursor hidden by default for immersion */
    html, body { height:100%; margin:0; cursor:none; }
    body {
      background:#000; color:#fff;
      font-family:"Courier New", monospace;
      font-size:0.9em; overflow:hidden;
    }

    /* Terminal layout: header at top, scrollable output, fixed input line */
    #terminal {
      display:flex; flex-direction:column; height:100%;
      padding:14px 20px 20px 20px; box-sizing:border-box;
    }

    /* Header mimics Python REPL banner */
    #header { margin-bottom:1em; white-space:pre-wrap; text-align:left; }

    /* Output area: hides scrollbars for realism, spacer prevents overlap with input */
    #output {
      flex:1 1 auto; white-space:pre-wrap; overflow-y:auto;
      scrollbar-width:none; padding-bottom:12px;
    }
    #output::-webkit-scrollbar { display:none; }
    #output::after { content:""; display:block; height:64px; }

    /* Input line: prompt + editable command span */
    #input-line {
      flex:0 0 auto; display:inline-flex; align-items:center;
      margin-top:8px; padding-top:4px; line-height:1em;
    }
    #prompt, #command {
      font-family:"Courier New", monospace;
      font-size:0.9em; line-height:1em;
      display:inline-flex; align-items:center;
    }
    #prompt { margin-right:6px; }
    #command {
      outline:none; white-space:pre; caret-color:transparent;
      min-width:1ch; flex:1 1 auto;
    }
    /* Zero-width space keeps line height stable when empty */
    #command:empty::before { content:"\200B"; visibility:hidden; }
    /* Custom blinking block cursor for terminal authenticity */
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
Welcome to Transaction Analyser

Options:

1. Print summary (type 'print')

2. Analyse transactions (type 'analyse')

3. Stop program (type 'stop')
    </div>

    <div id="input-line">
      <span id="prompt">>>> </span>
      <span id="command" contenteditable="true"></span>
    </div>
  </div>

  <!-- Python logic: dataset + functions for summary and analysis -->
  <script type="text/python" id="py-code">
data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

def print_summary(transactions):
    # Aggregate totals for deposits and withdrawals
    deposits = [t[0] for t in transactions if t[0] >= 0]
    withdrawals = [t[0] for t in transactions if t[0] <= 0]
    total_deposited, total_withdrawn = sum(deposits), sum(withdrawals)
    balance = total_deposited + total_withdrawn
    print("Summary:")
    print(f"  Deposited: {total_deposited:.2f}  Withdrawn: {total_withdrawn:.2f}  Balance: {balance:.2f}\n")

def analyse_transactions(transactions):
    # Print all transactions for transparency
    print("Transactions:")
    for amount, desc in transactions:
        print(f"  {amount:.2f}  {desc}")
    print()

    # Calculate averages separately for withdrawals and deposits
    withdrawals = [t[0] for t in transactions if t[0] <= 0]
    deposits = [t[0] for t in transactions if t[0] >= 0]
    avg_withdrawal = sum(withdrawals)/len(withdrawals) if withdrawals else 0
    avg_deposit = sum(deposits)/len(deposits) if deposits else 0

    # Sort to easily extract largest withdrawal and deposit
    transactions.sort()
    largest_withdrawal, largest_deposit = transactions[0], transactions[-1]

    print(f"  Avg withdrawal: {avg_withdrawal:.2f}  Avg deposit: {avg_deposit:.2f}")
    print(f"  Largest withdrawal: {largest_withdrawal}")
    print(f"  Largest deposit: {largest_deposit}\n")
  </script>

  <script>
    /* Header: emulates Python REPL banner with live timestamp */
    function formatDate() {
      const now = new Date();
      return `${now.toDateString()} ${now.getHours().toString().padStart(2,"0")}:${now.getMinutes().toString().padStart(2,"0")}`;
    }
    function updateHeader() {
      document.getElementById("header").textContent =
`Python 3.15.0 (main, ${formatDate()}) [Clang 14.0.0]
Type "help", "credits", "license" or "copyright"
for more information.`;
    }
    updateHeader(); setInterval(updateHeader, 1000); // refresh every second so minutes flip on time

    /* Initialize Pyodide and preload Python code to avoid first-command delay */
    let pyodide;
    async function initPyodide(){
      pyodide=await loadPyodide();
      await pyodide.runPythonAsync(document.getElementById("py-code").textContent);
      document.getElementById("command").classList.add("ready");
      document.getElementById("command").focus();
    }
    window.addEventListener("load",()=>{ initPyodide(); });

    /* Append text to output and auto-scroll to bottom */
    function appendAndStick(text) {
      const out = document.getElementById("output");
      out.textContent += text;
      out.scrollTop = out.scrollHeight;
    }

    /* Command router: maps user input to Python functions or built-in responses */
    async function runCommand(raw) {
      const cmd = raw.trim().toLowerCase();
      let output = "";
      pyodide.setStdout({ batched: s => output += s });

      if (cmd === "print") {
        await pyodide.runPythonAsync("print_summary(data)");
      } else if (cmd === "analyse") {
        await pyodide.runPythonAsync("analyse_transactions(data)");
      } else if (cmd === "help") {
        output = "Options:\n\nprint = show summary totals\nanalyse = show dataset, averages, largest values\nstop = end program";
      } else if (cmd === "credits") {
        output = "This was originally created on Mimo.";
      } else if (cmd === "copyright") {
        output = "Copyright (c) 2001-2025 Python Software Foundation.\nAll Rights Reserved.";
      } else if (cmd === "license") {
        output = "Python is distributed under the PSF License.\nSee https://docs.python.org/3/license.html for details.";
      } else if (cmd === "stop") {
        // Reset message instead of actually quitting, to keep demo interactive
        output = "Program stopped.\n\nOptions:\n\n1. Print summary (type 'print')\n\n2. Analyse transactions (type 'analyse')\n\n3. Stop program (type 'stop')";
      } else {
        output = "Invalid choice";
      }

      appendAndStick(`\n>>> ${cmd}\n\n${output}`);
    }

    /* Capture Enter key to submit commands; clear line after execution */
    const cmdEl=document.getElementById("command");
    cmdEl.addEventListener("keydown", async e=>{
      if(e.key==="Enter"){
        e.preventDefault();
        const raw=cmdEl.innerText;
        cmdEl.textContent="";
        await runCommand(raw);
      }
    });

    /* Cursor visibility: shown briefly on movement, hidden again for immersion */
    let cursorTimer=null;
    window.addEventListener("mousemove",()=>{
      document.body.style.cursor="default";
      clearTimeout(cursorTimer);
      cursorTimer=setTimeout(()=>{ document.body.style.cursor="none"; },1200);
    });
  </script>
</body>
</html>

