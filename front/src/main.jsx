import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import './assets/css/satoshi.css'
import App from './App.jsx'
import Song from './assets/songs/songa.mp3'
import BackgroundMusic from './BackgroundMusic.jsx'
createRoot(document.getElementById('root')).render(
  <StrictMode>
    <BackgroundMusic src={Song} />

    <App />
  </StrictMode>,
)
