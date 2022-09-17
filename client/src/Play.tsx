import React from "react";
import { useParams } from "react-router-dom";

export const Play: React.FC<{}> = () => {
  const id = useParams();
  console.log("id = ", id);
  return <div>play</div>;
};
