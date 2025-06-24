// Dice.jsx
import React from 'react';
import './Dice.css';
import { FaCrown } from "react-icons/fa6";
import Input from '@mui/material/Input';
import { useState } from 'react';
import './Components.css'
import { useNavigate } from "react-router";


const Login = ({ number }) => {
    let navigate = useNavigate();

    const [password, setPassword] = useState('')
    const [email, setEmail] = useState('');


    const handleSubmit = async (e) => {
        e.preventDefault();

        const data = { correo: email, contrasena: password };

        try {
            const response = await fetch('http://127.0.0.1:8000/login', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            const result = await response.json();
            console.log('Response from server:', result);

            if (response.ok) {
                console.log('Login successful:', result);
                localStorage.setItem('logged', true);
                localStorage.setItem('user', JSON.stringify(result));
                navigate('/');
            } else {
                console.error('Login failed:', result.message);
            }
        } catch (error) {
            console.error('Error sending login:', error);
        }
    };
    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%', padding: '20px' }}>
            <div style={{ textAlign: 'center', gap: '20px', justifyContent: 'center', backgroundColor: '#fee429', minWidth: '50%', border: '8px solid black', borderRadius: '8px', display: 'flex', flexDirection: 'column', alignItems: 'center', height: '100%' }}>
                <Input
                    className='input'
                    placeholder='correo'
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <Input
                    className='input'
                    placeholder='contrasena'
                    type='password'
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <div className='button' onClick={handleSubmit}>
                    Ingresar
                </div>
            </div >
        </div>
    );
};

export default Login;
