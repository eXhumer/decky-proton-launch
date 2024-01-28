import {
  PanelSection,
  definePlugin,
  staticClasses,
} from "decky-frontend-lib";
import { VFC } from "react";
import { FaShip } from "react-icons/fa";

const Content: VFC = () => {
  return (
    <PanelSection title="Proton Launch">
      <h1>Hello, World!</h1>
    </PanelSection>
  );
};

export default definePlugin(() => {
  return {
    title: <div className={staticClasses.Title}>Proton Launch</div>,
    icon: <FaShip />,
    content: <Content />,
  };
});
