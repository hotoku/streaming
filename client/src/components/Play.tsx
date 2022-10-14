import React, { useEffect } from "react";
import { useParams } from "react-router-dom";

export const Play: React.FC<{}> = () => {
  const params = useParams();
  const id = params["id"];
  let url = `/video/${id}`;

  useEffect(() => {
    const el = document.getElementById("player") as HTMLVideoElement;
    if (el) {
      el.load();
    }
  }, [url]);

  return (
    <video id="player" controls width="100%">
      <source src={url} type="video/mp4" />
    </video>
  );
};
