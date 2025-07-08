import { useState } from 'react'
import './App.scss'
import { AnimatedDice } from './Dice';
import TotalDice from './TotalDice';
import { useEffect } from 'react';
import { SiUmbraco } from "react-icons/si";
import Modal from './Modal';
import { useNavigate } from 'react-router';

function App() {
  const navigate = useNavigate();

  const [state, setState] = useState(null);
  const [user, setUser] = useState({})

  const [apuesta, setApuesta] = useState(100)
  const [playerDices, setPlayerDices] = useState([])
  const [dealerDices, setDealerDices] = useState([])
  const [status, setStatus] = useState('')
  const [dealerStatus, setDealerStatus] = useState('')

  const [totalPlayer, setTotalPlayer] = useState(0);
  const [totalDealer, setTotalDealer] = useState(0);
  const [hasBetDoubled, setHasBetDoubled] = useState(false)

  const [lostGameModalOpen, setLostGameModalOpen] = useState(false);
  const [wonGameModalOpen, setWonGameModalOpen] = useState(false);
  const [tieGameModalOpen, setTieGameModalOpen] = useState(false)
  const [blackjackGameModalOpen, setBlackjackGameModalOpen] = useState(false);

  useEffect(() => {
    const logged = localStorage.getItem('logged');
    if (logged) {
      const userData = JSON.parse(localStorage.getItem('user'));
      setUser(userData);
    }
  }, [])

  useEffect(() => {
    if (status === 'plantado') {
      dealerTurn(dealerDices)
    }
    if (status === 'pasado') {
      determineWinner(21)

      setLostGameModalOpen(true);
      setStatus('fin')
    }
    else if (status == 'blackjack') {
      setBlackjackGameModalOpen(true);
      setStatus('fin')
    }
    else if (status == 'fin') {
    }
  }, [status])

  const dealerTurn = async (dealerDices) => {
    const res = await fetch("http://127.0.0.1:8000/turnoCrupier", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(dealerDices)
    })
      .then(res => res.json())
      .then(data => {
        console.log(data);
        setDealerDices(data[1])
        setDealerStatus(data[0][0])
        setTotalDealer(data[0][1])
        determineWinner(data[0][1])
      })
  }

  const handleApuestaUp = () => {
    if (apuesta + 100 < user.saldo) {
      setApuesta(apuesta + 100)
    }
  }

  const handleApuestaDown = () => {
    if (apuesta == 100) return

    setApuesta(apuesta - 100)
  }
  const determineWinner = async (totalDealer) => {
    const data = { estado_jugador: status, total_jugador: totalPlayer, estado_crupier: dealerStatus, total_crupier: totalDealer };
    console.log('data', data);

    const res = await fetch("http://127.0.0.1:8000/determinarGanador", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(data => {
        calculateWinnings(data)
        if (data === 'victoria') {
          setWonGameModalOpen(true);
        }
        else if (data === 'derrota') {
          setLostGameModalOpen(true);
        }
        else if (data === 'empate') {
          setTieGameModalOpen(true);
        }
        else if (data === 'blackjack') {
          setBlackjackGameModalOpen(true);
        }
        setStatus('fin')

      })
  }

  const save = async (winnings) => {
    let user = JSON.parse(localStorage.getItem('user'));
    console.log('winninf', user.saldo);

    user.saldo += winnings;

    console.log('after', user.saldo);

    setUser(user)
    localStorage.setItem('user', JSON.stringify(user));

    const rex = await fetch("http://127.0.0.1:8000/guardarDatos", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(user)
    })
      .then(res => res.json())
      .then(data => {
      })


    const data = { nuevo_saldo: user.saldo, id_usuario: user.id };

    const res = await fetch("http://127.0.0.1:8000/nuevoSaldo", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(data => {
      })
  }

  const calculateWinnings = async (resultado) => {
    const data = { resultado: resultado, apuesta: apuesta, saldo: user.saldo };
    const res = await fetch("http://127.0.0.1:8000/calcularGanancias", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(data => {
        console.log('data', data);

        save(data)
      })
  }

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
        sumarDados([...playerDices, ...data])
        setPlayerDices([...playerDices, ...data])
        dealerDices.length < 1 && getDealerdices(2)
        evaularMano([...playerDices, ...data])
      })
  }

  const sumarDados = async (mano) => {
    const res = await fetch("http://127.0.0.1:8000/sumarDados", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(mano)
    })
      .then(res => res.json())
      .then(data => {
        setTotalPlayer(data);
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
        setStatus(data[0])
      })
  }

  const handlePlantarse = async () => {
    if (playerDices.length < 1) return;

    const data = { mano: playerDices, apuesta: apuesta, total: playerDices.reduce((partialSum, a) => partialSum + a, 0) };

    const res = await fetch("http://127.0.0.1:8000/plantarse", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(data => {
        setStatus(data[0])
      })
  }


  const handleDoblarApuesta = async () => {
    if (playerDices.length < 1 || hasBetDoubled) return;

    const data = { mano: playerDices, apuesta: apuesta, saldo: user.saldo };


    const res = await fetch("http://127.0.0.1:8000/doblarApuesta", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(data)
    })
      .then(res => res.json())
      .then(data => {

        setHasBetDoubled(true)
        setApuesta(data[1])
        setPlayerDices(data[0])
        sumarDados(data[0])
        setStatus(data[3])
      })
  }
  return (
    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%', padding: '20px' }}>
      <div style={{ textAlign: 'center', backgroundColor: '#fee429', minWidth: '60%', border: '8px solid black', borderRadius: '8px', display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%' }}>
        <div style={{ width: '100%', backgroundColor: '#ff60b1' }}>
          <h1 style={{ fontSize: '84px', margin: 0, fontFamily: 'Satoshi-Black', borderBottom: '8px solid black' }}>BLACKJACK DICE</h1>
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
              <TotalDice number={(status == '' || status == 'jugando') ? '?' : totalDealer} />
            </div>
          </div>
        </div>
        <div style={{ display: 'flex', width: '100%', flexDirection: 'row', height: '100%' }}>
          <div className='player-container' style={{ backgroundColor: '#26afff' }}>
            <div>
              {user.nombre}
            </div>
            <div style={{ fontSize: '24px', marginTop: '20px', display: 'flex', flexDirection: 'row', alignItems: 'center', gap: '5px' }}>
              Apostado: <SiUmbraco />{apuesta}
            </div>
            {playerDices.length < 1 &&
              <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'center', gap: '10px' }} onClick={() => { }}>
                <div onClick={handleApuestaDown} className='bet'>-</div>
                <div onClick={handleApuestaUp} className='bet'>+</div>
              </div>
            }

          </div>
          <div className='play-container'>
            <div className="dice-container">
              {playerDices.map((dice, index) => (
                <AnimatedDice key={`${index}-${dice}-player`} value={dice} isCroupier={false} />
              ))}
            </div>
            <div>
              <TotalDice number={totalPlayer} />
            </div>
          </div>
        </div>
      </div>
      <div style={{ height: '20%', backgroundColor: '#fee429', minWidth: '70%', border: '8px solid black', borderRadius: '8px', display: 'flex', justifyContent: 'center', flexDirection: 'column', alignItems: 'center', padding: '20px', marginTop: '20px' }}>
        {status === 'pasado' || status === 'fin' ?
          <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-between', width: '100%', alignItems: 'center', gap: '20px' }}>
            <div className={`button`} onClick={() => { location.reload() }}>{'Jugar otra vez'}</div>
            <div className={`button`} onClick={() => { navigate('/') }} style={{ backgroundColor: '#ff60b1' }}>{'Salir'}</div>
            <div className='button saldo' style={{ backgroundColor: '#26afff', borderRadius: '40px', display: 'flex', flexDirection: 'row', alignItems: 'center', gap: '5px' }}><SiUmbraco />{user.saldo}</div>
          </div>
          :
          <div style={{ display: 'flex', flexDirection: 'row', justifyContent: 'space-between', width: '100%', alignItems: 'center', gap: '20px' }}>
            <div className={`button`} onClick={() => getPlayerDices(playerDices.length < 1 ? 2 : 1)}>{playerDices.length < 1 ? 'Comenzar partida' : 'Pedir dado'}</div>
            <div className={`button ${playerDices.length < 1 || hasBetDoubled ? 'disabled' : ''}`} onClick={handleDoblarApuesta} style={{ backgroundColor: '#a487f0' }}>Doblar apuesta</div>
            <div className={`button ${playerDices.length < 1 ? 'disabled' : ''}`} onClick={handlePlantarse} style={{ backgroundColor: '#ff60b1' }}>Plantarse</div>
            <div className='button saldo' style={{ backgroundColor: '#26afff', borderRadius: '40px', display: 'flex', flexDirection: 'row', alignItems: 'center', gap: '5px' }}><SiUmbraco />{user.saldo}</div>
          </div>
        }



      </div>
      <Modal isOpen={lostGameModalOpen} onClose={() => { setLostGameModalOpen(false) }}>
        <div style={{ padding: '20px', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '20px', justifyContent: 'space-evenly' }}>
          <>

            <h2 style={{ fontSize: '48px' }}>Lo siento, has perdido.</h2>
            <h3 style={{ fontSize: '28px', display: 'flex', flexDirection: 'row', alignItems: 'center' }}>Tu nuevo saldo es de: <SiUmbraco />{user.saldo}</h3>
          </>
          <div className='button' onClick={() => { setLostGameModalOpen(false) }}>Cerrar</div>
        </div>
      </Modal>
      <Modal isOpen={blackjackGameModalOpen} onClose={() => { setBlackjackGameModalOpen(false) }}>
        <div style={{ padding: '20px', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '20px', justifyContent: 'space-evenly' }}>
          <>

            <h2 style={{ fontSize: '48px' }}>BLACKJACK. Has ganado!</h2>
            <h3 style={{ fontSize: '28px', display: 'flex', flexDirection: 'row', alignItems: 'center' }}>Tu nuevo saldo es de: <SiUmbraco />{user.saldo}</h3>
          </>
          <div className='button' onClick={() => { setBlackjackGameModalOpen(false) }}>Cerrar</div>
        </div>
      </Modal>
      <Modal isOpen={tieGameModalOpen} onClose={() => { setTieGameModalOpen(false) }}>
        <div style={{ padding: '20px', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '20px', justifyContent: 'space-evenly' }}>
          <>

            <h2 style={{ fontSize: '48px' }}>Has empatado.</h2>
            <h3 style={{ fontSize: '28px', display: 'flex', flexDirection: 'row', alignItems: 'center' }}>Tu nuevo saldo es de: <SiUmbraco />{user.saldo}</h3>
          </>
          <div className='button' onClick={() => { setTieGameModalOpen(false) }}>Cerrar</div>
        </div>
      </Modal>
      <Modal isOpen={wonGameModalOpen} onClose={() => { setWonGameModalOpen(false) }}>
        <div style={{ padding: '20px', textAlign: 'center', display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '20px', justifyContent: 'space-evenly' }}>
          <>

            <h2 style={{ fontSize: '48px' }}>Has ganado!.</h2>
            <h3 style={{ fontSize: '28px', display: 'flex', flexDirection: 'row', alignItems: 'center' }}>Tu nuevo saldo es de: <SiUmbraco />{user.saldo}</h3>
          </>
          <div className='button' onClick={() => { setWonGameModalOpen(false) }}>Cerrar</div>
        </div>
      </Modal>
      {blackjackGameModalOpen &&
        <>
          <div class="firework"></div>
          <div class="firework"></div>
          <div class="firework"></div>
        </>
      }
    </div>
  );
}



export default App
