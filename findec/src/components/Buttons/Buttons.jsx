/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import PropTypes from "prop-types";
import React from "react";
import { Icons24PxFb2 } from "../../icons/Icons24PxFb2";
import "./style.css";

export const Buttons = ({
  state,
  className,
  frameClassName,
  text = "Facebook",
  icon = <Icons24PxFb2 className="icons-fb" />,
  divClassName,
}) => {
  return (
    <div className={`buttons ${state} ${className}`}>
      <div className={`frame-4 ${frameClassName}`}>
        {state === "outline-icon" && (
          <>
            {icon}
            <div className={`facebook ${divClassName}`}>{text}</div>
          </>
        )}

        {["fill", "icon", "transparent"].includes(state) && (
          <div className="facebook-2">
            {["fill", "transparent"].includes(state) && <>{text}</>}

            {state === "icon" && <img className="oval" alt="Oval" src="/img/oval.svg" />}
          </div>
        )}
      </div>
    </div>
  );
};

Buttons.propTypes = {
  state: PropTypes.oneOf(["fill", "icon", "transparent", "outline-icon"]),
  text: PropTypes.string,
};
