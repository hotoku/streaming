import React from "react";
import { useParams } from "react-router-dom";

export const Play: React.FC<{}> = () => {
  const params = useParams();
  const id = params["id"];
  let url = `/video/${id}`;

  return (
    <video controls width="720">
      <source src={url} type="video/mp4" />
    </video>
  );
};
