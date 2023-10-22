import React from "react";
import { Form } from "../../components/Form";
import { LeftSide } from "../../components/LeftSide";
import { Icons24PxGoogle3 } from "../../icons/Icons24PxGoogle3";
import "./Signup.css";

export const SignUp = () => {
  return (
    <div className="sign-up">
      <div className="div-3">
        <LeftSide
          className="left-side-instance"
          device="desktop"
          text="81%"
          text1="of college students have not calculated how much they need to save for retirement"
          theme="dark"
        />
        <Form
          buttonsDivClassName="form-5"
          buttonsFrameClassName="form-2"
          buttonsFrameClassNameOverride="form-4"
          buttonsIcon={<Google className="icons-google" />}
          buttonsStateOutlineIconClassName="form-3"
          buttonsText="Sign up"
          buttonsText1="Returning user? Login Here"
          className="form-instance"
          inputsIconsEyeSubtract="subtract-3.svg"
          text="Sign Up"
          text1="Welcome!"
          theme="dark"
          type="login"
          visible={false}
          visible1={false}
        />
      </div>
    </div>
  );
};
