import React from 'react';
import { symbols } from './Utility';
function Grid({setStarted, started, symbol, grid, updateGrid, indexToCoord, coordToIndex, turn}) {


  function clickSquare(index) {
      if (!started || grid[index] !== '' || turn !== symbol) return;
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
  

    return (
        <div className="grid-container" id="tic-tac-toe-grid">
          {grid.map((value, index) => (
            <button
              key={index}
              onClick={() => clickSquare(index)}
              className="grid"
              disabled={value !== ''}
            >
              {value}
            </button>
          ))}
        </div>
    );
}

export default Grid;