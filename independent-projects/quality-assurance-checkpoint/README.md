## 🚩 Quality Assurance Checkpoint

### 📍 Context

Quality assurance is not only about identifying mistakes, it is about creating trust in the systems we design and maintain. In professional environments, errors are inevitable, but strong engineering practice is defined by the ability to surface them quickly, diagnose them clearly, and resolve them in ways that build confidence for both developers and reviewers.

This project demonstrates that principle in a transparent and reproducible way. The focus is not on formatting or naming conventions, but on the discipline of debugging and the structured reasoning that supports it. By deliberately introducing small but realistic bugs into Python scripts and documenting the process of diagnosing and fixing them, the project shows how quality assurance functions as a checkpoint in the development cycle.

The aim is to show that debugging is not an afterthought or a reactive scramble, but a structured practice that builds trust. To illustrate this, the project presents two examples: one simple logic error and one more complex Python‑specific pitfall. Each is designed to be small, self‑contained, and realistic, so that the process can be followed easily by both technical and non‑technical reviewers. In this way, the project demonstrates that quality assurance is a proactive discipline that strengthens the reliability of software systems.

---

### 🧪 Method
The method applied across the project follows a consistent cycle that reflects professional debugging practice:  

- **Step 1: Introduce a bug intentionally**  
  Each bug is chosen to represent a common category of error that developers encounter in real projects. The intention is not to create contrived mistakes but to highlight issues that are subtle enough to escape casual review yet significant enough to cause incorrect results.  

- **Step 2: Run the buggy script**  
  The script is executed in a Python terminal to observe its behaviour. This execution produces either an incorrect result or an error trace. Capturing this output is important because it provides evidence of the bug and a starting point for diagnosis.  

- **Step 3: Diagnose the root cause**  
  The diagnosis is performed by reasoning through the code line by line and explaining why the observed behaviour occurs. The explanation is not guesswork but a structured account grounded in Python semantics. The aim is to make the reasoning visible so that reviewers can follow the thought process.  

- **Step 4: Write a fixed version of the script**  
  The fixed code is written to the same quality standard as the buggy code. The difference lies only in the corrected logic. This ensures that the focus remains on the bug itself rather than on stylistic differences.  

- **Step 5: Validate the fix with automated tests**  
  Each example includes a minimal but sufficient test suite. The tests demonstrate that the bug is resolved and that the corrected behaviour is consistent across edge cases. The passing tests provide confidence that the fix is effective and that the function behaves as intended.  

This method ensures that the debugging process is transparent, reproducible, and easy to follow. It also demonstrates that quality assurance is not only about finding errors but about documenting the reasoning behind each correction. To illustrate this, the project includes one relatively simple bug - a loop logic error, and one relatively complex bug - a mutable default argument.

---

### 💬 Exposition

#### Example 1: Loop Logic Error  

The first example demonstrates a classic off‑by‑one error in a loop. In the [buggy script](https://github.com/musman-uk/portfolio/blob/main/independent-projects/quality-assurance-checkpoint/examples/example_1_loop_error/buggy_script.py), the function that computes an order total iterates one step too far, which results in an index error when it tries to access a non‑existent list element. The [fixed script](https://github.com/musman-uk/portfolio/blob/main/independent-projects/quality-assurance-checkpoint/examples/example_1_loop_error/fixed_script.py) corrects this by iterating directly over the items, ensuring that all elements are included without exceeding the list bounds. The [tests](https://github.com/musman-uk/portfolio/blob/main/independent-projects/quality-assurance-checkpoint/tests/test_example_1_loop_error.py) confirm that the corrected function produces the expected totals, even when orders are empty or contain multiple items. This example illustrates how a small logic error can produce runtime failures that halt execution. Such errors are particularly problematic because they may not be obvious at first glance. By capturing the incorrect output, diagnosing the cause, and validating the fix with tests, the project demonstrates how quality assurance can prevent these issues from persisting.  

<details>
<summary>View Terminal Outputs</summary>

Buggy Script:

```bash
$ python examples/example_1_loop_error/buggy_script.py
Traceback (most recent call last):
  File "examples/example_1_loop_error/buggy_script.py", line 29, in <module>
    print("Batch total:", compute_batch_total(orders))
  File "examples/example_1_loop_error/buggy_script.py", line 21, in compute_batch_total
    batch_total += compute_order_total(order)
  File "examples/example_1_loop_error/buggy_script.py", line 15, in compute_order_total
    line = items[i]
IndexError: list index out of range
```

Fixed Script:

```bash
$ python examples/example_1_loop_error/fixed_script.py
Batch total: 18.75
```

Tests:

```bash
$ pytest tests/test_example_1_loop_error.py -v
============================= test session starts ==============================
platform linux -- Python 3.11.9, pytest-8.2.0, pluggy-1.5.0
rootdir: /workspaces/quality-assurance-checkpoint
collected 2 items

tests/test_example_1_loop_error.py::test_compute_order_total_basic PASSED [ 50%]
tests/test_example_1_loop_error.py::test_compute_batch_total_with_empty_order PASSED [100%]

============================== 2 passed in 0.05s ===============================
```
</details>

#### Example 2: Mutable Default Argument  

This example highlights a Python‑specific pitfall: using a mutable default argument. In the [buggy script](https://github.com/musman-uk/portfolio/blob/main/independent-projects/quality-assurance-checkpoint/examples/example_2_mutable_default_argument/buggy_script.py), log entries unintentionally accumulate across function calls because the default list is shared. The [fixed script](https://github.com/musman-uk/portfolio/blob/main/independent-projects/quality-assurance-checkpoint/examples/example_2_mutable_default_argument/fixed_script.py) resolves this by using None as the default and creating a new list per call when needed. The [tests](https://github.com/musman-uk/portfolio/blob/main/independent-projects/quality-assurance-checkpoint/tests/test_example_2_mutable_default_argument.py) verify both behaviours: fresh state per call, correct extension of an existing list, and accurate summarisation.  This example demonstrates how subtle language features can introduce hard‑to‑spot issues. By contrasting outputs from the buggy and fixed implementations and validating with tests, the documentation makes the behaviour visible and the fix trustworthy.  

<details>
<summary>View Terminal Outputs</summary>

Buggy Script:

```bash
$ python examples/example_2_mutable_default_argument/buggy_script.py
=== Buggy Logging Demo ===
First call: ['Error: Disk full']
Second call: ['Error: Disk full', 'Warning: Low memory']
Third call: ['Error: Disk full', 'Warning: Low memory', 'Info: Job completed']
Summary: {'Error': 1, 'Warning': 1, 'Info': 1}
```

Fixed Script:

```bash
$ python examples/example_2_mutable_default_argument/fixed_script.py
=== Fixed Logging Demo ===
First call: ['Error: Disk full']
Second call: ['Warning: Low memory']
Third call: ['Info: Job completed']
Summary: {'Error': 1, 'Warning': 1, 'Info': 1}
```

Test:

```bash
$ pytest tests/test_example_2_mutable_default_argument.py -v
============================= test session starts ==============================
platform linux -- Python 3.11.9, pytest-8.2.0, pluggy-1.5.0
rootdir: /workspaces/quality-assurance-checkpoint
collected 3 items

tests/test_example_2_mutable_default_argument.py::test_each_call_starts_fresh PASSED [ 33%]
tests/test_example_2_mutable_default_argument.py::test_extend_existing_list PASSED [ 66%]
tests/test_example_2_mutable_default_argument.py::test_summary_counts PASSED     [100%]

============================== 3 passed in 0.04s ===============================
```
</details>

---

### 🌅 Afterword

The two examples illustrate how quality assurance transforms bugs into opportunities for clarity and trust. Observing the behaviour, capturing the output, diagnosing the cause, writing the fix, and validating with tests demonstrates the discipline of systematic debugging. By documenting both the error and the resolution, the project shows that debugging is not only about making code run, but about making the reasoning behind the fix visible. This transparency builds confidence for reviewers, collaborators, and future maintainers, while reducing the chance of repeating the same mistakes.

Quality assurance is a checkpoint, not an afterthought. It ensures that every piece of code contributes to a reliable system. By surfacing errors and resolving them with transparent tests, this project demonstrates how even small bugs can build confidence in the engineering process. The lessons extend beyond these examples. In larger systems the same cycle applies, even when bugs are more complex or traces harder to interpret. Quality assurance provides a structured way to move from failure to resolution, ensuring that fixes are both applied and explained.

This project serves as both a demonstration and a template. It shows how intentional bugs can be used to teach, to document, and to reinforce systematic debugging as a cornerstone of professional software engineering. Above all, it frames quality assurance as a proactive discipline that builds trust in the systems we create.

