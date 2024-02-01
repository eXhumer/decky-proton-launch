import {
  PanelSection,
  definePlugin,
  staticClasses,
} from "decky-frontend-lib";
import { VFC, useState } from "react";
import { FaShip } from "react-icons/fa";

const Content: VFC = () => {
  const [resp, setResp] = useState<string | null>(null);
  const backendWS = new WebSocket("ws://localhost:3000");

  backendWS.onopen = function() {
    console.log("[open] Connection established with backend");
    console.log("Sending \"Hello, world!\" to server");
    backendWS.send("Hello, world!");
  };

  backendWS.onmessage = function(event) {
    console.log(`[message] Data received from server: ${event.data}`);
    setResp(event.data);
  };

  return (
    <PanelSection title="Proton Launch">
      <h1>Hello, World!</h1>
      {resp !== null ?
        <h2>Backend Response: {resp}</h2> :
        null}
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
