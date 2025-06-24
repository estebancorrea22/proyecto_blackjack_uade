// Dice.jsx
import React from 'react';
import './Dice.css';
import { FaCrown } from "react-icons/fa6";

const Dice = ({ number }) => {
    const clamped = Math.max(1, Math.min(number, 10));
    const dots = getDotPositions(clamped);

    return (
        <div className="dice">
            {clamped === 10 ? (
                <div className="crown-wrapper">
                    <FaCrown className="crown-icon" />
                </div>
            ) : (
                <div className="grid">
                    {Array.from({ length: 9 }).map((_, i) => {
                        const isVisible = dots.includes(i);
                        const isSingle = dots.length === 1;
                        return (
                            <span
                                key={i}
                                className={`pip ${isVisible ? 'visible' : ''} ${isVisible && isSingle ? 'single' : ''}`}
                            />
                        );
                    })}
                </div>
            )}
        </div>
    );
};

const getDotPositions = (num) => {
    const patterns = {
        1: [4],
        2: [0, 8],
        3: [0, 4, 8],
        4: [0, 2, 6, 8],
        5: [0, 2, 4, 6, 8],
        6: [0, 2, 3, 5, 6, 8],
        7: [0, 2, 3, 4, 5, 6, 8],
        8: [0, 1, 2, 3, 5, 6, 7, 8],
        9: [0, 1, 2, 3, 4, 5, 6, 7, 8],
    };
    return patterns[num] || [4];
};

export default Dice;
