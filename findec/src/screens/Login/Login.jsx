import React from "react";
import { Form } from "../../components/Form";
import { LeftSide } from "../../components/LeftSide";
import { Icons24PxGoogle3 } from "../../icons/Icons24PxGoogle3";
import "./Login.css";

export const Login = () => {
  return (
    <div className="login">
      <div className="div-2">
        <LeftSide
          className="left-side-instance"
          device="desktop"
          text="81%"
          text1="of college students have not calculated how much they need to save for retirement"
          theme="dark"
        />
        {/* <div className='inputs'> 
            <div className='input'> 
                <img src={user_icon} alt="" />
                <input type="text" placeholder='User ID'/>
            </div>
            <div className='input'> 
                <img src={user_icon} alt="" />
                <input type="text" placeholder='Username'/>
            </div>
            <div className='input'> 
                <img src={password_icon} alt="" />
                {action === "Sign Up" ? <input type="password" placeholder='Create Password'/> : <input type="password" placeholder='Password'/>}
            </div>
        </div>
        {action === "Sign Up" ? <div></div> : <div className='forgot-password'> Forgot Password? <span>Click Here!</span></div>}
        <div className='submit-container'>
            <div className={action === "Login" ? "submit gray": "submit"} onClick={()=> {setaction("Sign Up")}}> Sign Up </div>
            <div className={action === "Sign Up" ? "submit gray": "submit"} onClick={()=> {setaction("Login")}}> Login </div>
        </div> */}
        <Form
          buttonsClassName="design-component-instance-node"
          buttonsFrameClassName="form-2"
          buttonsFrameClassNameOverride="form-4"
          buttonsIcon={<Icons24PxGoogle3 className="icons-px-google" />}
          buttonsStateOutlineIconClassName="form-3"
          buttonsText="New User? Sign Up Here"
          className="form-instance"
          theme="dark"
          type="login"
          visible={false}
          visible1={false}
        />
      </div>
    </div>
  );
};
