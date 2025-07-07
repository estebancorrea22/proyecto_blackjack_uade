import React from 'react'

const TotalDice = ({ number = '19' }) => {

    return (
        <div style={{ fontSize: '102px', color: 'black', fontFamily: 'Satoshi-Black' }}>
            {number}
        </div>
    );
};

export default TotalDice