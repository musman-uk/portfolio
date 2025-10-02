```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>🔢 Unit Converter</title>
  <style>
    /* Page foundation: dark background for strong contrast, consistent padding, and a neutral sans-serif font for readability */
    body {
      background-color: darkgreen;
      padding: 20px;
      font-family: Arial, sans-serif;
      margin: 0;
    }

    /* Title styled as a card: white background and rounded corners ensure visibility against the dark page */
    h1 {
      background-color: white;
      padding: 20px;
      border-radius: 20px;
    }

    /* Result container: fixed width and minimum height prevent layout shifts, while card styling separates output from inputs */
    p {
      background-color: white;
      color: black;
      border-radius: 20px;
      width: 300px;
      min-height: 30px;
      padding: 20px;
    }

    /* Inputs and button: consistent spacing and rounded edges improve usability and visual balance */
    input, select, button {
      margin: 10px 5px 20px 0;
      padding: 8px;
      border-radius: 6px;
      border: 1px solid #ccc;
      font-size: 1em;
    }

    /* Button: styled for affordance (looks clickable), with hover feedback to reinforce interactivity */
    button {
      cursor: pointer;
      background-color: #fff;
      border: 1px solid #333;
    }
    button:hover {
      background-color: #eee;
    }

    /* Footer credit: fixed in bottom-right, styled subtly so attribution is visible but doesn’t distract from main UI */
    footer {
      position: fixed;
      bottom: 8px;
      right: 12px;
      font-size: 0.75em;
      color: rgba(255,255,255,0.7); /* translucent white keeps it legible without dominating */
      text-shadow: 0 0 3px rgba(0,0,0,0.6); /* ensures readability even if background is light */
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>Unit Converter</h1>

  <!-- Numeric input: user provides the value to convert -->
  <input type="number" id="userInput" placeholder="Enter number..." />

  <!-- Dropdown: explicit choice of conversion direction avoids ambiguity -->
  <select id="unit">
    <option value="milesToKm">Miles to Kilometers</option>
    <option value="kmToMiles">Kilometers to Miles</option>
  </select>

  <!-- Button used instead of auto-convert: gives user control over when calculation runs -->
  <button onclick="convert()">Convert</button>

  <!-- Result display: updated dynamically with conversion output -->
  <p>Result: <span id="resultElement">0</span></p>

  <!-- Attribution footer -->
  <footer>
    Originally created and hosted via Mimo
  </footer>

  <script>
    // Conversion function: validates input, applies correct formula, and updates the result display
    function convert() {
      const inputValue = parseFloat(document.getElementById('userInput').value);
      const unit = document.getElementById('unit').value;
      const resultElement = document.getElementById('resultElement');

      // Guard clause: prevents invalid or empty input from producing misleading results
      if (isNaN(inputValue)) {
        resultElement.textContent = "Please enter a valid number.";
        return;
      }

      let result = 0;
      let resultString = "";

      // Case 1: Miles → Kilometers
      // Uses fixed conversion factor; pluralisation logic ensures grammatically correct output
      if (unit === 'milesToKm') {
        result = inputValue * 1.60934;
        const mileLabel = inputValue === 1 ? "mile" : "miles";
        const kmLabel = result === 1 ? "kilometer" : "kilometers";
        resultString = `${inputValue} ${mileLabel} equals ${result.toFixed(2)} ${kmLabel}`;

      // Case 2: Kilometers → Miles
      // Division by the same factor reverses the conversion; pluralisation applied again for clarity
      } else if (unit === 'kmToMiles') {
        result = inputValue / 1.60934;
        const kmLabel = inputValue === 1 ? "kilometer" : "kilometers";
        const mileLabel = result === 1 ? "mile" : "miles";
        resultString = `${inputValue} ${kmLabel} equals ${result.toFixed(2)} ${mileLabel}`;

      // Defensive fallback: ensures resilience if new options are ever added incorrectly
      } else {
        resultString = "Invalid conversion type selected.";
      }

      // Replace placeholder with final, contextualised result string
      resultElement.textContent = resultString;
    }
  </script>
</body>
</html>

