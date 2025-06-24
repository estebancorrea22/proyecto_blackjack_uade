import React, { useEffect } from 'react'
import { useState } from 'react';
import './Home.css';
import { Link, useNavigate } from 'react-router';

const Home = ({ }) => {
    const navigate = useNavigate();

    const [logged, setLogged] = useState(false)
    const [user, setuser] = useState({})

    useEffect(() => {
        let logged = localStorage.getItem('logged')
        if (logged) {
            setLogged(true)
            const userData = JSON.parse(localStorage.getItem('user'))
            setuser(userData)
        } else {
            setLogged(false)
        }

    }, [])

    const signOut = () => {
        localStorage.removeItem('logged');
        localStorage.removeItem('user');
        setLogged(false);
        setuser({});
        navigate('/');
    }

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%', padding: '20px' }}>
            <div style={{ fontSize: '102px', color: 'black', fontFamily: 'Satoshi-Black', backgroundColor: '#fee429', minWidth: '50%', border: '8px solid black', borderRadius: '8px', display: 'flex', flexDirection: 'column', justifyContent: 'space-around', alignItems: 'center', height: '100%' }}>
                <div className='shadow-dance-text' style={{ padding: '10px 30px' }}>Blackdice</div>
                {
                    logged ? (
                        <div style={{ fontSize: '32px', alignItems: 'center', display: 'flex', flexDirection: 'column', gap: '10px', height: '100px' }}>
                            <div>Bienvenido {user.nombre}</div>
                            <div>Saldo: {user.saldo}$</div>
                        </div>
                    ) : (
                        <>
                            <div style={{ fontSize: '48px', color: 'black', fontFamily: 'Satoshi-Black', padding: '15px', height: '100px' }}>
                                Inicia sesión para jugar
                            </div>
                        </>
                    )
                }

                {logged ? (
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'stretch', gap: '20px', marginTop: '20px', width: '405px', }}>
                        <div className='button' style={{ backgroundColor: '#ff60b1' }} onClick={() => { navigate('/play') }}>Jugar</div>
                        <div className='button' style={{ backgroundColor: '#65c93a' }}>Ver mi perfil</div>
                        <div className='button' style={{ backgroundColor: '#26afff' }}>Ver usuarios</div>
                        <div className='button' style={{ backgroundColor: '#a487f0' }} onClick={() => { signOut() }}>Cerrar Sesion</div>
                        {/* <div className='button' style={{ backgroundColor: '#ff6b6b' }}>Salir</div> */}
                    </div>
                ) : (
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'stretch', gap: '20px', marginTop: '20px', width: '405px', }}>
                        <Link to="/login" style={{ textDecoration: 'none', color: 'black' }}>
                            <div className='button' style={{ backgroundColor: '#ff60b1' }}>
                                Ingresar
                            </div>
                        </Link>

                        <div className='button' style={{ backgroundColor: '#65c93a' }}>Registrarse</div>
                        <div className='button' style={{ backgroundColor: '#26afff' }}>Ver usuarios</div>
                        {/* <div className='button' style={{ backgroundColor: '#ff6b6b' }}>Salir</div> */}
                    </div>
                )}
            </div>
        </div>
    );
};

export default Home