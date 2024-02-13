import React from 'react';
import { fadeIn, fadeOut } from './Utility' 



function Restart({setSymbol, setStarted, setGrid, setFirst}) {


    function handleRestartGame() {
        setSymbol(prevSymbol => {
            return ''; 
        });
        setFirst(prevFirst => {
            return ''; 
        });
        setStarted(false)
        setGrid(Array(9).fill(''));
        document.getElementById("winner").textContent="";
        fadeOut('restart').then(() => {
            fadeIn('buttons')
            fadeIn('symbol')
          });
    }

    return (
        <div className="restart-button" id="restart">
            <button onClick={handleRestartGame} className="button">Restart</button>
        </div>
    );
}
export default Restart;