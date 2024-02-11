import React from 'react';

function Grid({grid, clickSquare}) {
    return (
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
    );
}

export default Grid;