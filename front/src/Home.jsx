import React, { useEffect } from 'react'
import { useState } from 'react';
import './Home.css';
import { Link, useNavigate } from 'react-router';
import { SiUmbraco } from "react-icons/si";
import Modal from './Modal';

const Home = ({ }) => {
    const navigate = useNavigate();

    const [logged, setLogged] = useState(false)
    const [user, setuser] = useState({})
    const [isUsersModalOpen, setIsUsersModalOpen] = useState(false);
    const [users, setUsers] = useState([])

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

    const getUsers = async () => {
        const response = await fetch('http://127.0.0.1:8000/getUsers', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            },
        });
        const data = await response.json();
        console.log(data);
        setUsers(data);
        setIsUsersModalOpen(true);
    }

    const getMyUserData = async () => {
        console.log(user);

        // const response = await fetch(`http://127.0.0.1:8000/getUsers/${}`, {
        //     method: 'GET',
        //     headers: {
        //         'Content-Type': 'application/json',
        //     },
        // });
        // const data = await response.json();
        // console.log(data);
        // setUsers(data);
        // setIsUsersModalOpen(true);
    }


    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%', padding: '20px' }}>
            <div style={{ fontSize: '102px', color: 'black', fontFamily: 'Satoshi-Black', backgroundColor: '#fee429', minWidth: '50%', border: '8px solid black', borderRadius: '8px', display: 'flex', flexDirection: 'column', justifyContent: 'space-around', alignItems: 'center', height: '100%' }}>
                <div className='shadow-dance-text' style={{ padding: '10px 30px' }}>Blackdice</div>
                {
                    logged && user ? (
                        <div style={{ fontSize: '32px', alignItems: 'center', display: 'flex', flexDirection: 'column', gap: '10px', height: '100px' }}>
                            <div>Bienvenido {user.nombre}</div>
                            <div style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', gap: '5px' }}>Saldo: <SiUmbraco />{user.saldo}</div>
                        </div>
                    ) : (
                        <>
                            <div style={{ fontSize: '48px', color: 'black', fontFamily: 'Satoshi-Black', padding: '15px', height: '100px' }}>
                                Inicia sesión para jugar
                            </div>
                        </>
                    )
                }

                {logged && user ? (
                    <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'stretch', gap: '20px', marginTop: '20px', width: '405px', }}>
                        <div className='button' style={{ backgroundColor: '#ff60b1' }} onClick={() => { navigate('/play') }}>Jugar</div>
                        {/* <div className='button' style={{ backgroundColor: '#65c93a' }} onClick={() => { getMyUserData() }}>Ver mi perfil</div> */}
                        <div className='button' style={{ backgroundColor: '#26afff' }} onClick={() => { getUsers() }}>Ver usuarios</div>
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

                        {/* <div className='button' style={{ backgroundColor: '#65c93a' }}>Registrarse</div> */}
                        <div className='button' style={{ backgroundColor: '#26afff' }} onClick={() => { getUsers() }}>Ver usuarios</div>
                        {/* <div className='button' style={{ backgroundColor: '#ff6b6b' }}>Salir</div> */}
                    </div>
                )}
            </div>
            <Modal isOpen={isUsersModalOpen} onClose={() => { setIsUsersModalOpen(false) }}>
                {users.length > 0 && (
                    <div style={{ paddingTop: '20px' }}>
                        {users.map((user, index) => (
                            <div key={index} style={{ display: 'flex', flexDirection: 'row', alignItems: 'center', border: '4px solid black', borderRadius: '8px', marginBottom: '10px', backgroundColor: '#f9f9f9', justifyContent: 'space-between', padding: '10px' }}>
                                <div style={{ width: '100%', }} key={index}>
                                    <div style={{ fontSize: '24px', fontWeight: 'bold' }}>{user.nombre}</div>
                                    <div style={{ fontSize: '18px', display: 'flex', flexDirection: 'row', alignItems: 'center', gap: '4px' }}>Saldo: <SiUmbraco />{user.saldo}</div>
                                </div>
                                <div style={{ width: '100%' }} >
                                    <div style={{ fontSize: '18px', color: '#222' }}>Logros obtenidos: {user.logros?.logros_obtenidos?.length}</div>
                                </div>
                                <div style={{ width: '100%' }} >
                                    <div style={{ fontSize: '18px', color: '#222' }}>{user.correo}</div>
                                </div>
                            </div>

                        ))}
                    </div>
                )}
            </Modal>
        </div>
    );
};

export default Home