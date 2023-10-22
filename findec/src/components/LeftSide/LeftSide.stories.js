import { LeftSide } from ".";

export default {
  title: "Components/LeftSide",
  component: LeftSide,
  argTypes: {
    theme: {
      options: ["dark", "light"],
      control: { type: "select" },
    },
    device: {
      options: ["desktop", "mobile"],
      control: { type: "select" },
    },
  },
};

export const Default = {
  args: {
    theme: "dark",
    device: "desktop",
    className: {},
    text: "99%",
    text1: "of clients are satisfied ☺️ <br/>with our bank according <br/>to the survey",
  },
};
