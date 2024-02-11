import React, { useState } from 'react';
import './App.css';
import Grid from './Grid';
import Buttons from './Buttons';

function App() {
  const [started, setStarted] = useState(false);
  const [symbol, setSymbol] = useState('');
  const [grid, setGrid] = useState(Array(9).fill('')); 
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

  function updateGrid(index, player) {
    if (grid[index] !== '') return;
    setGrid(prevGrid => {
      const newGrid = [...prevGrid];
      newGrid[index] = player;
      return newGrid;
    });
  }
  
  return (
    <div className="App">    
      <header className="App-header">
        <Grid setStarted={setStarted} started={started} symbol={symbol} 
        grid={grid} updateGrid={updateGrid} indexToCoord={indexToCoord} 
        coordToIndex={coordToIndex} />
        <Buttons  setSymbol={setSymbol} symbol={symbol} 
          setStarted={setStarted} started={started} 
          setGrid={setGrid} coordToIndex={coordToIndex} 
          updateGrid={updateGrid} />
      </header>
    </div>
  );
}

export default App;