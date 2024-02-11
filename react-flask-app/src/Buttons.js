import React, { useState } from 'react';

function Buttons({setSymbol, symbol, setStarted, started, setGrid, coordToIndex, updateGrid}) {
    const [first, setFirst] = useState('');

    function handleRestartGame() {
        setSymbol('')
        setFirst('')
        setStarted(false)
        setGrid(Array(9).fill(''));
        document.getElementById("winner").textContent="";
    }
    function handleStart() {
        if (symbol === '' || first === '') return;
        fetch('./start')
          .then(response => {
            if (!response.ok) {
              throw new Error('Network response was not ok');
            }
            if (first !== symbol) {
              fetch('./move', {
                method: 'POST',
                headers: {
                  'Content-Type': 'application/json'
                }
              })
              .then(response => response.json()) 
              .then(response => {
                const [x, y] = response.opp_move.split(' ');
                updateGrid(coordToIndex(`${x} ${y}`), first);
              })
              .catch(error => {
                console.error('Error processing move:', error);
              });
            }
            setStarted(true);
          })
          .catch(error => {
            console.error('Network: fail', error);
          });
    }

    function handleFirstAndSymbol(route, sym) {
        if (started) return; 
    
        const data = {};
        if (route === './symbol') {
          data.symbol = sym;
          setSymbol(sym);
        } else if (route === './first') {
          data.first = sym;
          setFirst(sym);
        }
        return fetch(route, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(data)
        })
        .then(response => {
          if (!response.ok) {
            throw new Error('Network response was not ok');
          }
        })
        .catch(error => {
          console.error('Network: fail', error);
        });
    
    }
    return (
        <div>
            <div>
                <button onClick={handleStart} className="button-start" id="start">Start</button>
                <button onClick={handleRestartGame} className="button-restart" id="restart">Restart</button>
            </div>
            <div>
            <p id = "winner"></p>
            <header>Symbol?</header>
                <button onClick={() => handleFirstAndSymbol('./symbol', 'X')} className="button-start">X</button>
                <button onClick={() => handleFirstAndSymbol('./symbol', 'O')} className="button-start">O</button>
            <p>{symbol}</p>
            <header>First?</header>
                <button onClick={() => handleFirstAndSymbol('./first', 'X')} className="button-start">X</button>
                <button onClick={() => handleFirstAndSymbol('./first', 'O')} className="button-start">O</button>
            <p>{first}</p>
            </div>
        </div>
    );
}
export default Buttons;