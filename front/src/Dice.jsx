// Dice.jsx
import React from 'react';
import './Dice.css';

const Dice = ({ number }) => {
    // Cap number between 1 and 10
    const clamped = Math.max(1, Math.min(number, 10));

    return (
        <div className="dice">
            <div className="grid">
                {Array.from({ length: 9 }).map((_, i) => (
                    <span
                        key={i}
                        className={`pip ${getDotPositions(clamped).includes(i) ? 'visible' : ''}`}
                    />
                ))}
            </div>
        </div>
    );
};

const getDotPositions = (num) => {
    // 3x3 grid positions: index 0 to 8
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
        10: [0, 1, 2, 3, 4, 5, 6, 7, 8], // same as 9, plus maybe an animation or a border change to distinguish?
    };

    return patterns[num] || [4]; // fallback to 1
};

export default Dice;
