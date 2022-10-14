import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Style from "./Header.module.css";

export const Header = (): JSX.Element => {
  const [open, setOpen] = useState(false);
  const [targetNum, setVideoNum] = useState<number | undefined>();
  const navigate = useNavigate();

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
        <div>
          <input
            onChange={(e) => {
              setVideoNum(parseInt(e.target.value));
            }}
            value={targetNum || ""}
            type="number"
            min="1"
          />
        </div>
        <button
          onClick={() => {
            setOpen(false);
            navigate(`/play/${targetNum}`);
          }}
        >
          go
        </button>
        <button
          onClick={() => {
            setOpen(false);
          }}
        >
          cancel
        </button>
      </dialog>
    </div>
  );

  return (
    <header className={Style.header}>
      <button
        onClick={() => {
          navigate("/");
        }}
      >
        home
      </button>
      <button
        onClick={() => {
          setOpen(true);
        }}
      >
        jump
      </button>
      {dialog}
    </header>
  );
};
