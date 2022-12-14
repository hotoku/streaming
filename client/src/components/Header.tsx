import { useState } from "react";
import { useNavigate } from "react-router-dom";
import Style from "./Header.module.css";

export const Header = (): JSX.Element => {
  const [open, setOpen] = useState(false);
  const [targetNum, setTargetNum] = useState<number | undefined>();
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
              setTargetNum(parseInt(e.target.value));
            }}
            value={targetNum || ""}
            type="number"
            min="1"
          />
        </div>
        <button
          onClick={() => {
            setOpen(false);
            setTargetNum(undefined);
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
        className={Style.button}
        onClick={() => {
          navigate("/");
        }}
      >
        home
      </button>
      <button
        className={Style.button}
        onClick={() => {
          setOpen(true);
        }}
      >
        jump
      </button>
      <button
        onClick={() => {
          navigate("/upload");
        }}
      >
        upload
      </button>
      {dialog}
    </header>
  );
};
