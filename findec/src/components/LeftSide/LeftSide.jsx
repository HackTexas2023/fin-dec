/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import PropTypes from "prop-types";
import React from "react";
import { ElementsSeparator } from "../ElementsSeparator";
import "./style.css";

export const LeftSide = ({
  theme,
  device,
  className,
  text = "99%",
  text1 = "of clients are satisfied ☺️ <br/>with our bank according <br/>to the survey",
}) => {
  return (
    <div className={`left-side ${device} ${theme} ${className}`}>
      <div className="overlap-group">
        <div className="ellipse" />
        <div className="div" />
        <div className="ellipse-2" />
        <div className="ellipse-3" />
        <div className="ellipse-4" />
        <div className="ellipse-5" />
        <div className="frame">
          <div className="element">{text}</div>
          <p className="of-clients-are">{text1}</p>
        </div>
      </div>
      <div className="frame-2">
        <ElementsSeparator className="elements-separator-instance" />
        <ElementsSeparator className="instance-node" />
        <ElementsSeparator className="instance-node" />
      </div>
    </div>
  );
};

LeftSide.propTypes = {
  theme: PropTypes.oneOf(["dark", "light"]),
  device: PropTypes.oneOf(["desktop", "mobile"]),
  text: PropTypes.string,
  text1: PropTypes.string,
};
