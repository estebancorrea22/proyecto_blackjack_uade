import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import DiceScene, { AnimatedDice } from './Dice';
import Dice from './Dice';
import TotalDice from './TotalDice';
import Home from './Home';
import Login from './Login';
import { useEffect } from 'react';
import { SiUmbraco } from "react-icons/si";
import Modal from './Modal';

function App() {
  const [state, setState] = useState(null);
  const [user, setUser] = useState({})

  const [playerDices, setPlayerDices] = useState([])
  const [dealerDices, setDealerDices] = useState([])
  const [status, setStatus] = useState('')

  const [lostGameModalOpen, setLostGameModalOpen] = useState(false);
  const [blackjackGameModalOpen, setBlackjackGameModalOpen] = useState(false);

  useEffect(() => {
    const logged = localStorage.getItem('logged');
    if (logged) {
      const userData = JSON.parse(localStorage.getItem('user'));
      setUser(userData);
    }
  }, [])

  useEffect(() => {
    if (status === 'pasado') {
      setLostGameModalOpen(true);
    }
    else if (status == 'blackjack') {
      alert('¡Felicidades! Has ganado con un Blackjack.');
    }
  }, [status])



  const getDealerdices = async (dices) => {
    const res = await fetch("http://127.0.0.1:8000/tirarDados", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(dices)
    })
      .then(res => res.json())
      .then(data => {
        setDealerDices([...dealerDices, ...data])
      })
  }

  const getPlayerDices = async (dices) => {
    const res = await fetch("http://127.0.0.1:8000/tirarDados", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(dices)
    })
      .then(res => res.json())
      .then(data => {
        setPlayerDices([...playerDices, ...data])
        dealerDices.length < 1 && getDealerdices(2)
        evaularMano([...playerDices, ...data])
      })
  }

  const evaularMano = async (mano) => {
    const res = await fetch("http://127.0.0.1:8000/evaluarMano", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(mano)
    })
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setStatus(data[0])
      })
  }

  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%', padding: '20px' }}>
      <div style={{ textAlign: 'center', backgroundColor: '#fee429', minWidth: '60%', border: '8px solid black', borderRadius: '8px', display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%' }}>
        <div style={{ width: '100%', backgroundColor: '#ff60b1' }}>
          <h1 style={{ fontSize: '84px', margin: 0, fontFamily: 'Satoshi-Black', borderBottom: '8px solid black' }}>BLACKJACK</h1>
        </div>
        <div style={{ display: 'flex', width: '100%', flexDirection: 'row', height: '100%', borderBottom: '8px solid black' }}>
          <div className='player-container' style={{ backgroundColor: '#65c93a' }}>DEALER</div>
          <div className='play-container'>
            <div className="dice-container">
              {dealerDices.map((dice, index) => (
                <AnimatedDice key={`${index}-${dice}-player`} value={dice} isHidden={(status == '' || status == 'jugando') && index == 0} isCroupier={false} />
              ))}
            </div>
            <div>
              <TotalDice number={(status == '' || status == 'jugando') ? '?' : dealerDices.reduce((partialSum, a) => partialSum + a, 0)} />
            </div>
          </div>
        </div>
        <div style={{ display: 'flex', width: '100%', flexDirection: 'row', height: '100%' }}>
          <div className='player-container' style={{ backgroundColor: '#26afff' }}>
            <div>
              {user.nombre}
            </div>
            <div style={{ fontSize: '24px', marginTop: '20px', display: 'flex', flexDirection: 'row', alignItems: 'center', gap: '5px' }}>
              Apostado: <SiUmbraco />100
            </div>

          </div>
          <div className='play-container'>
            <div className="dice-container">
              {playerDices.map((dice, index) => (
                <AnimatedDice key={`${index}-${dice}-player`} value={dice} isCroupier={false} />
              ))}
            </div>
            <div>
              <TotalDice number={playerDices.reduce((partialSum, a) => partialSum + a, 0)} />
            </div>
          </div>
        </div>
      </div>
      <div style={{ height: '20%', backgroundColor: '#fee429', minWidth: '70%', border: '8px solid black', borderRadius: '8px', display: 'flex', justifyContent: 'center', flexDirection: 'column', alignItems: 'center', padding: '20px', marginTop: '20px' }}>
        <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-between', width: '100%', alignItems: 'center', gap: '20px' }}>
          <div className={`button`} onClick={() => getPlayerDices(playerDices.length < 1 ? 2 : 1)}>{playerDices.length < 1 ? 'Comenzar partida' : 'Pedir dado'}</div>
          <div className={`button ${playerDices.length < 1 ? 'disabled' : ''}`} style={{ backgroundColor: '#a487f0' }}>Doblar apuesta</div>
          <div className={`button ${playerDices.length < 1 ? 'disabled' : ''}`} style={{ backgroundColor: '#ff60b1' }}>Plantarse</div>
          <div className='button saldo' style={{ backgroundColor: '#26afff', borderRadius: '40px', display: 'flex', flexDirection: 'row', alignItems: 'center', gap: '5px' }}><SiUmbraco />{user.saldo}</div>
        </div>
      </div>
      <Modal isOpen={lostGameModalOpen} onClose={() => { setLostGameModalOpen(false) }}>
        <div style={{ padding: '20px', textAlign: 'center' }}>
          <h2>Lo siento, has perdido.</h2>
          <div className='button' onClick={() => { setLostGameModalOpen(false) }}>Cerrar</div>
        </div>
      </Modal>
    </div>
  );
}



export default App
