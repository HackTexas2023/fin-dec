import { Buttons } from ".";

export default {
  title: "Components/Buttons",
  component: Buttons,
  argTypes: {
    state: {
      options: ["fill", "icon", "transparent", "outline-icon"],
      control: { type: "select" },
    },
  },
};

export const Default = {
  args: {
    state: "fill",
    className: {},
    frameClassName: {},
    text: "Facebook",
    divClassName: {},
  },
};
