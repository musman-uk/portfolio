```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>🔐 Caesar Cipher</title>
  <style>
    /* Global styles: serif font for a classical feel, dark theme for contrast and readability */
    body {
      font-family: "Cambria", serif;
      background-color: #0C2828;
      color: #AAB8C2;
      margin: 0;
      padding: 20px;
    }

    /* Headings: light text with underline to separate sections visually */
    h2, h3 {
      color: #EFF2F7;
      border-bottom: 2px solid #2C3E50;
      padding-bottom: 5px;
    }

    label {
      display: block;
      margin: 20px 0 5px 0;
      font-weight: bold;
    }

    #output {
      margin: 20px;
      font-size: 1.1em;
    }

    /* Inputs and textarea: styled to match dark theme, with clear focus state for accessibility */
    input,
    textarea {
      box-sizing: border-box;
      width: 85%;
      margin: 0 20px 10px 0;
      padding: 10px;
      font-size: 18px;
      border: 1px solid #2C3E50;
      border-radius: 5px;
      background-color: #2C3E50;
      color: #EFF2F7;
    }

    input:focus,
    textarea:focus {
      border: 1px solid #3498DB; /* blue accent signals active input */
      outline: none;
    }

    /* Footer: fixed credit, styled subtly so it remains visible without distracting from the tool */
    footer {
      position: fixed;
      bottom: 8px;
      right: 12px;
      font-size: 0.8em;
      color: #ffffff;
      text-shadow: 0 0 2px rgba(0,0,0,0.8);
      font-family: Arial, sans-serif;
      font-weight: 500;
    }
  </style>
</head>
<body>
  <h2>Caesar Cipher</h2>

  <!-- Shift input: user chooses rotation amount; constrained to 1–25 to avoid trivial/no-op cases -->
  <label for="shift">Shift (1-25):</label>
  <input type="number" id="shift" value="1" min="1" max="25" />

  <!-- Plaintext input: freeform text area for encoding -->
  <label for="plaintext">Enter your text:</label>
  <textarea
    id="plaintext"
    rows="4"
    cols="50"
    placeholder="Enter your text here..."
  ></textarea>

  <!-- Output: dynamically updated with translated text -->
  <h3>Translated text</h3>
  <p id="output"></p>

  <!-- Attribution footer -->
  <footer>
    Originally created and hosted via Mimo
  </footer>

  <script>
    // Core Caesar cipher: shifts alphabetic characters by 'shift' positions, preserving case
    function caesarCipher(str, shift) {
      return str.replace(/[a-zA-Z]/g, function(c) {
        const base = c < 'a' ? 65 : 97; // ASCII base differs for uppercase vs lowercase
        return String.fromCharCode((c.charCodeAt(0) - base + shift) % 26 + base);
      });
    }

    // Translate: reads input values, applies cipher, and updates the output element
    function translate() {
      const plaintextValue = document.getElementById('plaintext').value;
      const shiftValue = parseInt(document.getElementById('shift').value);
      const outputValue = caesarCipher(plaintextValue, shiftValue);
      document.getElementById('output').textContent = outputValue;
    }

    // Live translation: updates output immediately as user types or changes shift value
    document.getElementById('plaintext').addEventListener('input', translate);
    document.getElementById('shift').addEventListener('input', translate);
  </script>
</body>
</html>
