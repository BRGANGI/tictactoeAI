import React, { useState, useEffect, useRef } from 'react';
import './App.css';

function App() {
  const [started, setStarted] = useState(false);
  const [name, setName] = useState('');
  const [first, setFirst] = useState('');
  const [symbol, setSymbol] = useState(''); 
  const [grid, setGrid] = useState(Array(9).fill('')); 

  useEffect(() => {
    // Effect logic can be added here if needed
  }, []);

  function clickSquare(index) {
    if (!started || grid[index] !== '') return;
    
    const newGrid = [...grid];
    newGrid[index] = symbol; 
    setGrid(newGrid);
  }

  function handleStart() {
    setStarted(true);
    fetch('/start')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
    })
    .catch(error => {
      console.error('Network: fail', error);
    });
  }

  function handleRestartGame() {
    setGrid(Array(9).fill(''));
    handleStart();
  }

  function handleConfirm() {
    fetch('/name', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: name })
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

  function handleFirstAndSymbol(route, sym) {
    const data = {};
    if (route === './symbol') {
      data.symbol = sym;
    } else if (route === './first') {
      data.first = sym;
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
          <input onChange={e => setName(e.target.value)} type="text" value={name} placeholder="Enter your name" />
          <button onClick={handleConfirm} id="setname">Confirm</button>
        </div>
        <div>
          <p>Symbol?</p>
          <button onClick={() => handleFirstAndSymbol('./symbol', 'X').then(symbol => setSymbol('X'))} className="button-start" id="xSymbol">X</button>
          <button onClick={() => handleFirstAndSymbol('./symbol', 'O').then(symbol => setSymbol('O'))} className="button-start" id="oSymbol">O</button>
        </div>
        <div>
          <p>First?</p>
          <button onClick={() => handleFirstAndSymbol('./first', 'X').then(first => setFirst('X'))} className="button-start" id="xFirst">X</button>
          <button onClick={() => handleFirstAndSymbol('./first', 'O').then(first => setFirst('O'))} className="button-start" id="oFirst">O</button>
        </div>
      </header>
    </div>
  );
}

export default App;
