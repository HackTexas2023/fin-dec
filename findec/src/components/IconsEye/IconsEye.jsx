/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import PropTypes from "prop-types";
import React from "react";
import "./style.css";

export const IconsEye = ({ className, subtract = "/img/subtract-8.svg" }) => {
  return (
    <div className={`icons-eye ${className}`}>
      <img className="subtract" alt="Subtract" src={subtract} />
    </div>
  );
};

IconsEye.propTypes = {
  subtract: PropTypes.string,
};
