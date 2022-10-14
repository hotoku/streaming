import { useState } from "react";
import Style from "./Header.module.css";

export const Header = (): JSX.Element => {
  const [open, setOpen] = useState(false);
  const dialog = (
    <div
      style={{
        position: "fixed",
        top: 0,
        left: 0,
        width: "100%",
        height: "100%",
        display: open ? "block" : "none",
        backgroundColor: "rgba(0,0,0,0.5)",
      }}
    >
      <dialog open={open}>
        <div>modal</div>
        <button
          onClick={() => {
            setOpen(false);
          }}
        >
          close
        </button>
      </dialog>
    </div>
  );

  return (
    <header className={Style.header}>
      <button
        onClick={() => {
          setOpen(true);
          console.log("jump");
        }}
      >
        jump
      </button>
      {dialog}
    </header>
  );
};
