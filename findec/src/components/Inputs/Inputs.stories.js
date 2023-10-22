import { Inputs } from ".";

export default {
  title: "Components/Inputs",
  component: Inputs,
  argTypes: {
    theme: {
      options: ["dark", "light"],
      control: { type: "select" },
    },
    state: {
      options: ["error", "input", "normal"],
      control: { type: "select" },
    },
  },
};

export const Default = {
  args: {
    theme: "dark",
    state: "error",
    className: {},
  },
};
