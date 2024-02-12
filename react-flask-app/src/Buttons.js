import React, { useState, useEffect } from 'react';
import {fadeOut, fadeIn} from './Utility' 



function Buttons({setSymbol, symbol, started, setStarted, setGrid, coordToIndex, updateGrid, setTurn}) {
    const [first, setFirst] = useState('');
    
    useEffect(() => {
      if (first !== '' && symbol !== '' && !started) {
        setTurn(first);
        handleStart();
      }
      }, [first, symbol, started, handleStart, setTurn]);
      // useEffect(() => {
      //       console.log("Sym", symbol);
      // }, [symbol]);

      // useEffect(() => {
      //   console.log("First", first);
      // }, [first]);


    function handleRestartGame() {
        setSymbol('')
        setFirst('')
        setStarted(false)
        setGrid(Array(9).fill(''));
        document.getElementById("winner").textContent="";
    }


    function handleStart() {
      fadeOut('first').then(() => {
        fadeOut('buttons'); 
      });

        return fetch('./start')
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
          setSymbol(prevSymbol => {
              data.symbol = sym;
              return sym; 
          });
          fadeOut('symbol').then(() => {
            fadeIn('first'); 
          });
      } else if (route === './first') {
          setFirst(prevFirst => {
              data.first = sym;
              return sym; 
          });
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
        <div className="button-container" id="buttons">
            <div class="restart-button" id="restart">
                {/* <button onClick={handleStart} className="button" id="start">Start</button> */}
                <button onClick={handleRestartGame} className="button">Restart</button>
            </div>
            <div className="symbol-button-container">
              <div id='symbol'>
                <header>Symbol?</header>
                <button onClick={() => handleFirstAndSymbol('./symbol', 'X')} className="button">X</button>
                <button onClick={() => handleFirstAndSymbol('./symbol', 'O')} className="button">O</button>
              </div>
              <div id='first'>
                <header>First?</header>
                <button onClick={() => handleFirstAndSymbol('./first', 'X')} className="button">X</button>
                <button onClick={() => handleFirstAndSymbol('./first', 'O')} className="button">O</button>
              </div>
            </div>
        </div>
    );
}
export default Buttons;