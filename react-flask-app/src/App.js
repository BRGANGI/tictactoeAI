import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [started, setStarted] = useState(false);
  const [first, setFirst] = useState('');
  const [symbol, setSymbol] = useState('');
  const [grid, setGrid] = useState(Array(9).fill('')); 
  const [turn, setTurn] = useState('');
  const BOARD_DIM = 3;

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
    console.log("Grid changed", grid);
  }, [grid]);

  function clickSquare(index) {
    if (!started || grid[index] !== '') return;
    updateGrid(index, symbol);
    const moveData = { coord: indexToCoord[index] };
    
    var aiMoveIndex;
    
    fetch('./move', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(moveData)
    })
    .then(response => response.json())
    .then(response => {
      const [x, y] = response.opp_move.split(' ');
      aiMoveIndex = coordToIndex(`${x} ${y}`);
      updateGrid(aiMoveIndex, symbols[symbol]);
      changeTurn(turn);
    })
    .catch(error => {
      console.error('Error processing move:', error);
    });
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
      setTurn(sym);
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
      })
      .catch(error => {
        console.error('Network: fail', error);
      });
    
    setStarted(true);
  }

  function changeTurn(cur) {
    setTurn(cur => (cur === 'X' ? 'O' : 'X'));
  }

  function xyToIndex(x, y) {
    x = parseInt(x, 10);
    y = parseInt(y, 10);
    var index = (BOARD_DIM - y - 1) * BOARD_DIM + x;
    return index;
  }

  function indexToXY(index) {
    var x = index % BOARD_DIM;
    var y = Math.floor(index / BOARD_DIM);
    return `${x} ${y}`;
}
  

  return (
    <div className="App">    
      <header className="App-header">
        <div className="grid-container" id="tic-tac-toe-grid">
          {grid.map((value, index) => (
            <button
              key={index}
              onClick={() => clickSquare(index)}
              className="button-grid"
              disabled={value !== ''}
            >
              {value}
            </button>
          ))}
        </div>
        <div>
          <button onClick={handleStart} className="button-start" id="start">Start</button>
          <button onClick={handleRestartGame} className="button-restart" id="restart">Restart</button>
        </div>
        <div>
          <header>Symbol?</header>
          <button onClick={() => handleFirstAndSymbol('./symbol', 'X')} className="button-start" id="xSymbol">X</button>
          <button onClick={() => handleFirstAndSymbol('./symbol', 'O')} className="button-start" id="oSymbol">O</button>
          <p>{symbol}</p>
          <header>First?</header>
          <button onClick={() => handleFirstAndSymbol('./first', 'X')} className="button-start" id="xFirst">X</button>
          <button onClick={() => handleFirstAndSymbol('./first', 'O')} className="button-start" id="oFirst">O</button>
          <p>{first}</p>
        </div>

      </header>
    </div>
  );
}

export default App;