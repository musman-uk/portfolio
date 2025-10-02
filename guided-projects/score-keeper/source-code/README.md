```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>🏆 Score Keeper</title>
  <!-- React + ReactDOM via CDN: chosen for simplicity so the demo runs without a build step -->
  <script src="https://unpkg.com/react@18/umd/react.development.js" crossorigin></script>
  <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js" crossorigin></script>
  <!-- Babel included to transpile JSX in-browser; acceptable for demos, not production -->
  <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  <style>
    /* Base page: light, neutral palette and centered text keep focus on the score UI */
    body {
      background-color: lightcyan;
      font-family: Arial, sans-serif;
      color: darkslategray;
      text-align: center;
      margin: 0;
      padding: 0;
    }

    /* Main container: card styling creates a focal point and reduces visual clutter */
    .score-keeper-container {
      background-color: white;
      text-align: center;
      margin: 20px auto;
      width: 80%;
      max-width: 640px;
      padding: 20px;
      border-radius: 10px;
      box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    /* Heading: teal accent establishes hierarchy and consistent theme */
    .score-keeper-heading {
      color: teal;
      font-size: 2.5em;
      margin-bottom: 20px;
    }

    /* Buttons: strong affordance with consistent sizing and spacing */
    .score-keeper-button {
      margin: 10px;
      padding: 10px 20px;
      font-size: 1em;
      color: white;
      background-color: teal;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    /* Hover state: darker shade provides immediate feedback */
    .score-keeper-button:hover {
      background-color: darkslategray;
    }

    /* Leading highlight: visually distinguishes whichever team is ahead */
    .score-view-wrapper-leading-true {
      color: white;
      background-color: teal;
      border-radius: 5px;
      padding: 5px;
      margin: 5px auto;
      width: fit-content;
    }

    /* Footer: fixed, subtle credit that remains visible without distracting from the app */
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
  <div id="root"></div>

  <!-- Attribution footer for transparency -->
  <footer>
    Originally created and hosted via Mimo
  </footer>

  <script type="text/babel">
    // ScoreView: stateless component that renders a team's score.
    // "leading" prop controls a highlight style, separating presentation from logic.
    const ScoreView = (props) => {
      return (
        <div className={`score-view-wrapper-leading-${props.leading}`}>
          <h2>
            {props.teamName}: {props.score}
          </h2>
        </div>
      );
    };

    // ScoreKeeper: stateful component managing both team's scores.
    // React hooks ensure updates are isolated and predictable; resetScores centralizes reset logic.
    const ScoreKeeper = () => {
      const [teamOneScore, setTeamOneScore] = React.useState(0);
      const [teamTwoScore, setTeamTwoScore] = React.useState(0);

      const resetScores = () => {
        setTeamOneScore(0);
        setTeamTwoScore(0);
      };

      return (
        <div className="score-keeper-container">
          <h1 className="score-keeper-heading">Score Keeper</h1>
          <ScoreView
            teamName="Team One"
            score={teamOneScore}
            leading={teamOneScore > teamTwoScore}
          />
          <button
            className="score-keeper-button"
            onClick={() => setTeamOneScore(teamOneScore + 1)}
          >
            +1 Team One
          </button>
          <ScoreView
            teamName="Team Two"
            score={teamTwoScore}
            leading={teamTwoScore > teamOneScore}
          />
          <button
            className="score-keeper-button"
            onClick={() => setTeamTwoScore(teamTwoScore + 1)}
          >
            +1 Team Two
          </button>
          <br />
          <button
            className="score-keeper-button"
            onClick={resetScores}
          >
            Reset Scores
          </button>
        </div>
      );
    };

    // App: minimal root component for clarity and separation of concerns
    const App = () => {
      return <ScoreKeeper />;
    };

    // Explicit mount into root keeps the demo portable and easy to embed in any HTML page
    const root = ReactDOM.createRoot(document.getElementById("root"));
    root.render(<App />);
  </script>
</body>
</html>
