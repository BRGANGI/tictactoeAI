import React, { useState, useEffect } from 'react';
import './App.css';
import Grid from './Grid';
import Buttons from './Buttons';



function App() {
  const [started, setStarted] = useState(false);
  const [first, setFirst] = useState('');
  const [symbol, setSymbol] = useState('');
  const [grid, setGrid] = useState(Array(9).fill('')); 

  const symbols = {
    'X': 'O',
    'O': 'X'
  }
  const indexToCoord = {
    0: "0 2",
    1: "1 2",
    2: "2 2",
    3: "0 1",
    4: "1 1",
    5: "2 1",
    6: "0 0",
    7: "1 0",
    8: "2 0"
  }

  function coordToIndex(coord) {
    return Object.keys(indexToCoord).find(key => indexToCoord[key] === coord);
  }



  useEffect(() => {

  }, []);

  function clickSquare(index) {
    if (!started || grid[index] !== '') return;
    updateGrid(index, symbol);
    const moveData = { coord: indexToCoord[index] };
        
    fetch('./move', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(moveData)
    })
    .then(response => response.json())
    .then(response => {
      console.log("Response: ", response);
      if (response.opp_move === '') {
        handleWin(response.winner);
      }
      const [x, y] = response.opp_move.split(' ');

      updateGrid(coordToIndex(`${x} ${y}`), symbols[symbol]);
      if (response.winner !== '') {
        handleWin(response.winner);
      }
    })
    .catch(error => {
      console.error('Error processing move:', error);
    });
  }
  
  function handleWin(winner) {
    setStarted(false);
    if (winner === 'tie') {
      document.getElementById("winner").textContent="It's a tie";
    } else {
      document.getElementById("winner").textContent=`${winner} has won`;
    }
  }

  function updateGrid(index, player) {
    if (grid[index] !== '') return;
    setGrid(prevGrid => {
      const newGrid = [...prevGrid];
      newGrid[index] = player;
      return newGrid;
    });
  }

  function handleRestartGame() {
    setSymbol('')
    setFirst('')
    setStarted(false)
    setGrid(Array(9).fill(''));
    document.getElementById("winner").textContent="";
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


  return (
    <div className="App">    
      <header className="App-header">
        <Grid grid={grid} clickSquare={clickSquare} />
<Buttons handleStart={handleStart} handleRestartGame={handleRestartGame} handleFirstAndSymbol={handleFirstAndSymbol} symbol={symbol} first={first} />

      </header>
    </div>
  );
}

export default App;