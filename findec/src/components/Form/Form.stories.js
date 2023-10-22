import { Form } from ".";

export default {
  title: "Components/Form",
  component: Form,
  argTypes: {
    theme: {
      options: ["dark", "light"],
      control: { type: "select" },
    },
    type: {
      options: ["login", "result"],
      control: { type: "select" },
    },
  },
};

export const Default = {
  args: {
    theme: "dark",
    type: "login",
    className: {},
    visible: true,
    buttonsClassName: {},
    buttonsFrameClassName: {},
    buttonsText: "Forgot your password?",
    buttonsStateOutlineIconClassName: {},
    visible1: true,
    buttonsFrameClassNameOverride: {},
  },
};
