## 🧩 Quality Assurance Checkpoint

### 📍 Context

Quality assurance is not only about identifying mistakes, it is about creating trust in the systems that we design and maintain. In professional environments, errors are inevitable, but what distinguishes strong engineering practice is not the absence of errors but the ability to surface them quickly, diagnose them clearly, and resolve them in a way that builds confidence for both developers and reviewers.  

This project was created to demonstrate that principle in a transparent and reproducible way. The focus is not on issues such as formatting or naming conventions, but  on the discipline of debugging and the structured reasoning that underpins it. By deliberately introducing small but realistic bugs into Python scripts and then documenting the process of diagnosing and fixing them, the project illustrates how quality assurance functions as a checkpoint in the development cycle.  

The aim is to show that debugging is not an afterthought or a reactive scramble. It is a structured practice that builds trust. Each example is designed to be small, self contained, and realistic, so that the workflow can be followed easily by both technical and non technical reviewers. In this way, the project demonstrates that quality assurance is a proactive discipline that strengthens the reliability of software systems.  

---

### 🧪 Method
The method applied across the project follows a consistent cycle that reflects professional debugging practice.  

The first step is to introduce a bug intentionally. Each bug is chosen to represent a common category of error that developers encounter in real projects. The intention is not to create contrived mistakes but to highlight issues that are subtle enough to escape casual review yet significant enough to cause incorrect results.  

The second step is to run the buggy script in a Python terminal. This execution produces either an incorrect result or an error trace. Capturing this output is important because it provides evidence of the bug and a starting point for diagnosis.  

The third step is to diagnose the root cause. This is done by reasoning through the code line by line and explaining why the observed behaviour occurs. The diagnosis is not guesswork but a structured explanation grounded in Python semantics. The aim is to make the reasoning visible so that reviewers can follow the thought process.  

The fourth step is to write a fixed version of the script. The fixed code is written to the same quality standard as the buggy code. The difference lies only in the corrected logic. This ensures that the focus remains on the bug itself rather than on stylistic differences.  

The fifth and final step is to validate the fix with automated tests. Each example includes a minimal but sufficient test suite. The tests demonstrate that the bug is resolved and that the corrected behaviour is consistent across edge cases. The passing tests provide confidence that the fix is effective and that the function behaves as intended.  

This method ensures that the debugging process is transparent, reproducible, and easy to follow. It also demonstrates that quality assurance is not only about finding errors but about documenting the reasoning behind each correction.  

---

### 💬 Exposition

#### Example 1: Loop Logic Error
The first example demonstrates a classic off by one error in a loop. The buggy script attempts to compute the total cost of an order by iterating over its items, but it mistakenly skips the final element. The result is an undercounted total that does not match the expected value.  

The fixed version corrects the loop logic by iterating directly over the items, ensuring that all elements are included. The associated tests confirm that the corrected function produces the expected totals, even when orders are empty or contain multiple items.  

This example illustrates how a small logic error can produce incorrect results without raising an exception. Such errors are particularly dangerous because they may go unnoticed until they cause significant discrepancies in calculations. By capturing the incorrect output, diagnosing the cause, and validating the fix with tests, the project demonstrates how quality assurance can prevent these errors from persisting.  

   [View Example 1 Buggy and Fixed Code]()  
   [View Example 1 Tests]()  

The expected test results show two passing cases. One test validates the basic computation of an order total. The other test validates the handling of an empty order within a batch. Together, they confirm that the fix resolves the bug and that the function behaves correctly across different scenarios.  

#### Example 2: Mutable Default Argument
The second example highlights a Python specific pitfall: the use of a mutable default argument. The buggy function appends log messages to a list, but because the default list is shared across calls, messages accumulate unexpectedly. This behaviour is subtle and can easily confuse developers who are not aware of how Python handles default arguments.  

The fixed version introduces a `None` default and creates a new list inside the function when needed. This ensures that each call starts fresh unless an explicit list is provided. The associated tests confirm that the function behaves correctly in both scenarios: starting fresh each time and appending to an existing list when passed.  

This example demonstrates how language specific features can introduce bugs that are not obvious at first glance. It also shows the importance of tests in making such behaviour visible. Without tests, the accumulation of log messages might not be noticed until it causes incorrect results in production.  

  [View Example 2 Buggy and Fixed Code]()  
  [View Example 2 Tests]()  

The expected test results show three passing cases. One test validates that each call starts fresh. Another test validates that an existing list can be extended. A third test validates that log messages can be summarised correctly. Together, they confirm that the fix resolves the bug and that the function behaves as intended.  

---

### 🌅 Afterword

These two examples illustrate how quality assurance transforms small failures into opportunities for clarity and trust. The bugs themselves are simple, but the workflow is what matters. The process of observing the behaviour, capturing the incorrect output, diagnosing the cause, writing the fix, and validating the correction with tests demonstrates the discipline of systematic debugging.  By documenting both the failure and the resolution, the project shows that debugging is not only about making code run. It is about making the reasoning behind the fix visible. This transparency builds confidence for reviewers, collaborators, and future maintainers. It also ensures that the same mistakes are less likely to be repeated.  

Quality assurance is a checkpoint, not an afterthought. It ensures that every piece of code contributes to a reliable and trustworthy system. By intentionally surfacing logic errors and resolving them with transparent tests, this project demonstrates how even small bugs can be leveraged to build confidence in the engineering process.  The lessons extend beyond these small examples. In larger systems, the same cycle applies. Bugs may be more complex, and the traces may be harder to interpret, but the principle remains the same. Quality assurance provides a structured way to move from failure to resolution. It ensures that fixes are not only applied but also explained and validated.  

This project therefore serves both as a demonstration and as a template. It shows how intentional bugs can be used to teach, to document, and to reinforce the value of systematic debugging as a cornerstone of professional software engineering. It also shows that quality assurance is not a reactive task but a proactive discipline that builds trust in the systems we create.  
