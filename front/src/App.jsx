import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import DiceScene from './Dice';
import Dice from './Dice';
import TotalDice from './TotalDice';
import Home from './Home';
import Login from './Login';
import { useEffect } from 'react';

function App() {
  const [state, setState] = useState(null);
  const [user, setUser] = useState({})

  const [playerDices, setPlayerDices] = useState([1, 5, 3])
  const [dealerDices, setDealerDices] = useState([10, 1])

  useEffect(() => {
    const logged = localStorage.getItem('logged');
    if (logged) {
      const userData = JSON.parse(localStorage.getItem('user'));
      setUser(userData);
    }
  }, [])


  const startGame = async () => {
    const res = await fetch("http://127.0.0.1:8000/start", { method: "POST" });
    const data = await res.json();
    setState(data);
    console.log(data);

  };

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%', padding: '20px' }}>
      {/* <Home /> */}
      {/* <Login /> */}
      <div style={{ textAlign: 'center', backgroundColor: '#fee429', minWidth: '50%', border: '8px solid black', borderRadius: '8px', display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%' }}>
        <div style={{ width: '100%', backgroundColor: '#ff60b1' }}>
          <h1 style={{ fontSize: '84px', margin: 0, fontFamily: 'Satoshi-Black', borderBottom: '8px solid black' }}>BLACKJACK</h1>
        </div>
        <div style={{ display: 'flex', width: '100%', flexDirection: 'row', height: '100%', borderBottom: '8px solid black' }}>
          <div className='player-container' style={{ backgroundColor: '#65c93a' }}>DEALER</div>
          <div className="dice-container">
            {dealerDices.map((dice, index) => (
              <Dice key={index} number={dice} />
            ))}
            <TotalDice number={dealerDices.reduce((partialSum, a) => partialSum + a, 0)} />
          </div>
        </div>
        <div style={{ display: 'flex', width: '100%', flexDirection: 'row', height: '100%' }}>
          <div className='player-container' style={{ backgroundColor: '#26afff' }}>
            <div>
              {user.nombre}
            </div>
            <div style={{ fontSize: '24px', marginTop: '20px' }}>
              Apostado: 100$
            </div>

          </div>
          <div className="dice-container">
            {playerDices.map((dice, index) => (
              <Dice key={index} number={dice} />
            ))}
            <TotalDice number={playerDices.reduce((partialSum, a) => partialSum + a, 0)} />
          </div>
        </div>
      </div>
      <div style={{ height: '20%', backgroundColor: '#fee429', minWidth: '50%', border: '8px solid black', borderRadius: '8px', display: 'flex', justifyContent: 'center', flexDirection: 'column', alignItems: 'center', padding: '20px', marginTop: '20px' }}>
        <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-between', width: '100%', alignItems: 'center' }}>
          <div className='button'>Pedir Carta</div>
          <div className='button' style={{ backgroundColor: '#ff60b1' }}>Plantarse</div>
          <div className='button saldo' style={{ backgroundColor: '#26afff', borderRadius: '40px' }}>${user.saldo}</div>
        </div>
      </div>

    </div>
  );
}



export default App
