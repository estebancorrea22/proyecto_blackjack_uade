import React, { useEffect, useRef } from 'react';

const BackgroundMusic = ({ src }) => {
    const audioRef = useRef(null);

    useEffect(() => {
        const audio = audioRef.current;

        // Attempt to autoplay if user has interacted
        const playAudio = () => {
            audio.play().catch(() => {
                console.warn("Autoplay blocked");
            });
            window.removeEventListener('click', playAudio);
        };

        window.addEventListener('click', playAudio); // iOS/Chrome requires user interaction

        return () => {
            window.removeEventListener('click', playAudio);
        };
    }, []);

    return (
        <audio ref={audioRef} src={src} loop preload="auto" />
    );
};

export default BackgroundMusic;
