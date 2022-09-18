import React from "react";
import { useParams, useSearchParams } from "react-router-dom";

export const Play: React.FC<{}> = () => {
  const params = useParams();
  const id = params["id"];
  const path = params["path"];
  let url = `/video/${id}`;
  if (path) {
    url += `?path=${window.atob(path)}`;
  }
  console.log(`id=${id}, path=${path}, url=${url}`);

  return (
    <video controls width="720">
      <source src={url} type="video/mp4" />
    </video>
  );
};
