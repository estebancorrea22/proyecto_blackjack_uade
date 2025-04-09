import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [state, setState] = useState(null);

  const startGame = async () => {
    const res = await fetch("http://127.0.0.1:8000/start", { method: "POST" });
    const data = await res.json();
    setState(data);
    console.log(data);

  };

  return (
    <div>
      <h1>Blackjack</h1>
      <button onClick={startGame}>Empezar</button>
    </div>
  );
}



export default App
