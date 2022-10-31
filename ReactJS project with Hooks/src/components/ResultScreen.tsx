import React, { FC } from 'react';

interface ResultScreenProps {
  result: string;
  closeResultHandler: () => void;
}

enum CoinTossPossibilities {
  DEFAULT = 'default',
  HEADS = 'heads',
  TAILS = 'tails',
  SIDE = 'side',
}

const ResultScreen: FC<ResultScreenProps> = ({
  result,
  closeResultHandler,
}) => {
  return (
    <div className="result-screen-background">
      <div className="result-screen">
        <div className="close-button-container">
          <button className="close-button" onClick={() => closeResultHandler()}>
            X
          </button>
        </div>
        <div>
          <p>Results</p>
          <div className="result-container">
            <span>
              {/* The following conditional rendering section will display 
              different emojis and text depending on the result that is passed 
              down to this component as a prop*/}
              {result === CoinTossPossibilities.HEADS && (
                <span className="icon"> &#128483;&#65039;</span>
              )}
              {result === CoinTossPossibilities.TAILS && (
                <span className="icon">&#129418;</span>
              )}
              {result === CoinTossPossibilities.SIDE && (
                <div className="result-container">
                  <span className="icon">&#127881;</span>
                  <p>
                    You have witnessed the rare occurence of the coin landing on
                    it's side
                  </p>
                </div>
              )}
            </span>
            <span>{result}</span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultScreen;
