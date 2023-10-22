/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import React from "react";
import { Icons24PxError3 } from "../../icons/Icons24PxError3";
import "./style.css";

export const Message = ({ className }) => {
  return (
    <div className={`message ${className}`}>
      <div className="frame-6">
        <Icons24PxError3 className="icons-error" />
        <p className="text-wrapper-5">
          Oops, your email or password is incorrect. Please try again or contact support.
        </p>
      </div>
    </div>
  );
};
