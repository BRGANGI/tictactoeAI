import React from 'react';

function Buttons({handleStart, handleRestartGame, handleFirstAndSymbol, symbol, first}) {
    return (
        <div>
            <div>
            <button onClick={handleStart} className="button-start" id="start">Start</button>
            <button onClick={handleRestartGame} className="button-restart" id="restart">Restart</button>
            </div>
            <div>
            <p id = "winner"></p>
            <header>Symbol?</header>
            <button onClick={() => handleFirstAndSymbol('./symbol', 'X')} className="button-start" id="xSymbol">X</button>
            <button onClick={() => handleFirstAndSymbol('./symbol', 'O')} className="button-start" id="oSymbol">O</button>
            <p>{symbol}</p>
            <header>First?</header>
            <button onClick={() => handleFirstAndSymbol('./first', 'X')} className="button-start" id="xFirst">X</button>
            <button onClick={() => handleFirstAndSymbol('./first', 'O')} className="button-start" id="oFirst">O</button>
            <p>{first}</p>
            </div>
        </div>
    );
}
export default Buttons;