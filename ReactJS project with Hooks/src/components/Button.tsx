import React, { FC } from 'react';

interface ButtonProps {
  beginGameHandler: () => void;
}

const Button: FC<ButtonProps> = ({ beginGameHandler }) => {
  return (
    <button className="button" onClick={() => beginGameHandler()}>
      Toss
    </button>
  );
};

export default Button;
