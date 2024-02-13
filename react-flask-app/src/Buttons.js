import React, { useEffect } from 'react';
import {fadeOut, fadeIn} from './Utility' 



function Buttons({setSymbol, symbol, started, setStarted, setGrid, coordToIndex, updateGrid, setTurn, first, setFirst}) {
    
    useEffect(() => {
      if (first !== '' && symbol !== '' && !started) {
        setTurn(first);
        handleStart();
      }
      }, [first, symbol, started, handleStart, setTurn]);

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
          data.symbol = sym;
          setSymbol(sym)
          fadeOut('symbol').then(() => {
            fadeIn('first'); 
          });
      } else if (route === './first') {
          data.first = sym;
          setFirst(sym)
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