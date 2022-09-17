import React from "react";
import { useParams, useSearchParams } from "react-router-dom";

export const Play: React.FC<{}> = () => {
  const params = useParams();
  const [sparams, setSparams] = useSearchParams();
  console.log("id = ", params["id"]);
  console.log("path = ", sparams.get("path"));

  return <div>play</div>;
};
