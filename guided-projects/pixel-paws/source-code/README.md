```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>🐾 Pixel Paws</title>
  <style>
    /* Global styles: simple, playful palette and centered layout to keep focus on the pets */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      background-color: lightskyblue;
      margin: 0;
      padding: 0;
    }

    h1 {
      margin-top: 20px;
      color: darkslategray;
    }

    /* Pet container: flex layout allows pets to wrap and stay evenly spaced */
    .pet-container {
      display: flex;
      flex-wrap: wrap;
      justify-content: space-around;
      margin-top: 40px;
    }

    /* Individual pet card: styled as a clickable tile with hover feedback via border */
    .pet {
      cursor: pointer;
      background-color: white;
      border-radius: 8px;
      padding: 12px;
      margin: 12px;
      width: 240px;
      transition: border 0.2s ease;
    }

    /* Selected pet: teal border provides clear visual feedback of active choice */
    .pet.selected {
      border: 3px solid teal;
    }

    .emoji {
      font-size: 50px;
      margin-top: 10px;
    }

    /* Treats container: horizontally centered row of treat options */
    .treat-container {
      display: flex;
      justify-content: center;
      margin-top: 30px;
    }

    .treat-wrapper {
      margin: 0 20px;
    }

    /* Treats: enlarged on hover to reinforce interactivity */
    .treat {
      font-size: 40px;
      cursor: pointer;
      transition: transform 0.2s ease;
    }

    .treat:hover {
      transform: scale(1.2);
    }

    /* Footer: fixed credit, styled subtly so it’s visible without distracting from gameplay */
    footer {
      position: fixed;
      bottom: 8px;
      right: 12px;
      font-size: 0.8em;
      color: #ffffff; /* solid white for clarity */
      text-shadow: 0 0 2px rgba(0,0,0,0.8); /* crisp outline for readability */
      font-family: Arial, sans-serif;
      font-weight: 500;
    }
  </style>
</head>
<body>
  <h1>Pixel Paws</h1>

  <!-- Pet selection area: players choose which pet to interact with -->
  <div class="pet-container">
    <div class="pet" id="pet1" onclick="selectPet(1)">
      <div class="emoji">&#128049;</div>
      <p>Saturation Level: <span id="hunger1">100</span>%</p>
      <p id="message1"></p>
    </div>
    <div class="pet" id="pet2" onclick="selectPet(2)">
      <div class="emoji">&#128054;</div>
      <p>Saturation Level: <span id="hunger2">100</span>%</p>
      <p id="message2"></p>
    </div>
  </div>

  <!-- Treats: different amounts of food to feed the selected pet -->
  <div class="treat-container">
    <div class="treat-wrapper">
      <div class="emoji treat" onclick="feedPet(1)">🍖</div>
    </div>
    <div class="treat-wrapper">
      <div class="emoji treat" onclick="feedPet(5)">🎂</div>
    </div>
  </div>

  <!-- Attribution footer -->
  <footer>
    Originally created and hosted via Mimo
  </footer>

  <script>
    /* Pet class: encapsulates state and behavior for each pet instance */
    class Pet {
      constructor(id) {
        this.id = id;
        this.fedLevel = 100;
        this.fedElement = document.getElementById(`hunger${id}`);
        this.messageElement = document.getElementById(`message${id}`);
        this.displayElement = document.getElementById(`pet${id}`);
      }

      // Feeding increases saturation; capped at 100 to prevent overflow
      feed(amount) {
        this.fedLevel += amount;
        if (this.fedLevel > 100) this.fedLevel = 100;
        this.fedElement.textContent = this.fedLevel;
      }

      // Hunger mechanic: decreases saturation periodically and updates UI state
      decreaseFedLevel() {
        this.fedLevel -= 10;
        if (this.fedLevel < 0) this.fedLevel = 0;
        this.fedElement.textContent = this.fedLevel;

        // When saturation hits zero, pet “runs away” (visual + message feedback)
        if (this.fedLevel === 0) {
          this.messageElement.textContent = "Pet ran away";
          this.displayElement.style.opacity = 0.5;
        } else {
          this.messageElement.textContent = "";
          this.displayElement.style.opacity = 1;
        }
      }
    }

    /* Global state: track which pet is currently selected */
    let selectedPet = null;
    const petElement1 = document.getElementById("pet1");
    const petElement2 = document.getElementById("pet2");

    const pet1 = new Pet(1);
    const pet2 = new Pet(2);

    // Selection logic: ensures only one pet is active at a time
    function selectPet(id) {
      petElement1.classList.remove("selected");
      petElement2.classList.remove("selected");

      selectedPet = id;
      if (id === 1) {
        petElement1.classList.add("selected");
      } else {
        petElement2.classList.add("selected");
      }
    }

    // Feeding logic: routes treat to whichever pet is currently selected
    function feedPet(amount) {
      if (selectedPet === 1) {
        pet1.feed(amount);
      } else if (selectedPet === 2) {
        pet2.feed(amount);
      }
    }

    // Game loop: decreases fed levels every 5 seconds to simulate time passing
    setInterval(() => {
      pet1.decreaseFedLevel();
      pet2.decreaseFedLevel();
    }, 5000);

    // Default state: Pet 1 is selected on load for immediate interaction
    selectPet(1);
  </script>
</body>
</html>
