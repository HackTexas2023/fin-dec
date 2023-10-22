/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import PropTypes from "prop-types";
import React from "react";
import { IconsEye } from "../IconsEye";
import "./style.css";

export const Inputs = ({ theme, state, className }) => {
  return (
    <div className={`inputs ${state} theme-0-${theme} ${className}`}>
      {["input", "normal"].includes(state) && (
        <>
          <IconsEye
            className={`${
              theme === "light" && state === "normal"
                ? "class"
                : theme === "dark" && state === "input"
                ? "class-2"
                : theme === "light" && state === "input"
                ? "class-3"
                : "class-4"
            }`}
            subtract={theme === "light" ? "/img/subtract-7.svg" : "/img/subtract-6.svg"}
          />
          <div className="text">
            {state === "normal" && <>Password</>}

            {state === "input" && (
              <>
                <div className="text-wrapper">Password</div>
                <div className="rectangle" />
              </>
            )}
          </div>
        </>
      )}

      {state === "error" && (
        <>
          <div className="input-2">
            <IconsEye
              className={`${theme === "light" ? "class-3" : "class-2"}`}
              subtract={theme === "light" ? "/img/subtract-7.svg" : "/img/subtract-6.svg"}
            />
            <div className="frame-3">
              <div className="text-2">Password</div>
              <div className="rectangle" />
            </div>
          </div>
          <p className="p">
            Invalid email address. <br />
            Email must contain the “@” symbol.
          </p>
        </>
      )}
    </div>
  );
};

Inputs.propTypes = {
  theme: PropTypes.oneOf(["dark", "light"]),
  state: PropTypes.oneOf(["error", "input", "normal"]),
};
