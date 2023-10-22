/*
We're constantly improving the code you see. 
Please share your feedback here: https://form.asana.com/?k=uvp-HPgd3_hyoXRBw1IcNg&d=1152665201300829
*/

import PropTypes from "prop-types";
import React from "react";
import { Icons24PxFb2 } from "../../icons/Icons24PxFb2";
import { Icons24PxGoogle3 } from "../../icons/Icons24PxGoogle3";
import { Icons72PxTick } from "../../icons/Icons72PxTick";
import { Icons72PxTick1 } from "../../icons/Icons72PxTick1";
import { Buttons } from "../Buttons";
import { ElementsSeparator } from "../ElementsSeparator";
import { Inputs } from "../Inputs";
import { Message } from "../Message";
import "./style.css";

export const Form = ({
  theme,
  type,
  className,
  visible = true,
  buttonsClassName,
  buttonsFrameClassName,
  buttonsText = "Forgot your password?",
  buttonsStateOutlineIconClassName,
  visible1 = true,
  buttonsIcon = <Icons24PxGoogle3 className="icons-google" />,
  buttonsFrameClassNameOverride,
}) => {
  return (
    <div className={`form type-${type} theme-5-${theme} ${className}`}>
      {type === "login" && (
        <div className="group">
          <div className="text-3">
            <div className="title">Log in</div>
            <div className="body">Welcome back!</div>
          </div>
        </div>
      )}

      {type === "result" && theme === "dark" && <Icons72PxTick className="icons-tick" />}

      {(theme === "dark" || type === "login") && (
        <div className="inputs-2">
          {type === "login" && (
            <>
              <>{visible && <Message className="message-instance" />}</>
              <div className="inputs-px">
                <div className="text-4">E-mail</div>
              </div>
              <Inputs className="inputs-56px" state="normal" theme={theme === "light" ? "light" : "dark"} />
            </>
          )}

          {type === "result" && (
            <>
              <div className="title-2">Log in</div>
              <div className="body-2">Welcome back!</div>
            </>
          )}
        </div>
      )}

      {theme === "light" && type === "result" && (
        <>
          <Icons72PxTick1 className="icons-px-tick" />
          <div className="text-5">
            <div className="title-3">Log in</div>
            <div className="body-3">Welcome back!</div>
          </div>
        </>
      )}

      {type === "result" && (
        <>
          <Buttons className="buttons-56px" frameClassName="buttons-px" state="fill" text="Login" />
          <p className="text-6">
            <span className="span">Did not receive the email? Check your spam filter, or</span>
            <span className="text-wrapper-2">&nbsp;</span>
            <span className="text-wrapper-3">Try another email address.</span>
          </p>
        </>
      )}

      {type === "login" && (
        <>
          <div className={`buttons-2 ${buttonsClassName}`}>
            <Buttons className="buttons-56px" frameClassName="buttons-px" state="fill" text="Login" />
            <Buttons
              className={buttonsStateOutlineIconClassName}
              frameClassName={buttonsFrameClassName}
              state="transparent"
              text={buttonsText}
            />
          </div>
          <div className="frame-5">
            <div className="divider">
              <ElementsSeparator className={`${theme === "light" ? "class-5" : "class-6"}`} />
              <div className="text-wrapper-4">OR</div>
              <ElementsSeparator className={`${theme === "light" ? "class-5" : "class-6"}`} />
            </div>
            <div className="social-buttons">
              {visible1 && (
                <Buttons
                  className={`${theme === "light" ? "class-7" : "class-6"}`}
                  divClassName={`${theme === "light" && "class-8"}`}
                  frameClassName="buttons-instance"
                  icon={<Icons24PxFb2 className="icons-google" />}
                  state="outline-icon"
                  text="Facebook"
                />
              )}

              <Buttons
                className={`${theme === "light" ? "class-7" : "class-6"}`}
                divClassName={`${theme === "light" && "class-8"}`}
                frameClassName={buttonsFrameClassNameOverride}
                icon={buttonsIcon}
                state="outline-icon"
                text="Google"
              />
            </div>
          </div>
        </>
      )}
    </div>
  );
};

Form.propTypes = {
  theme: PropTypes.oneOf(["dark", "light"]),
  type: PropTypes.oneOf(["login", "result"]),
  visible: PropTypes.bool,
  buttonsText: PropTypes.string,
  visible1: PropTypes.bool,
};
