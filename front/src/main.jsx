import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import './assets/css/satoshi.css'
import App from './App.jsx'
import Song from './assets/songs/songa.mp3'
import BackgroundMusic from './BackgroundMusic.jsx'
import { BrowserRouter, Route, Routes } from "react-router";
import Login from './Login.jsx'
import Home from './Home.jsx'
import { Toaster } from 'sonner'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BackgroundMusic src={Song} />
    <Toaster richColors closeButton />

    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/play" element={<App />} />

      </Routes>
    </BrowserRouter>
  </StrictMode>,
)
