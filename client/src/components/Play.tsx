import React, { useEffect, useRef } from "react";
import { useParams } from "react-router-dom";

export const Play: React.FC<{}> = () => {
  const params = useParams();
  const id = params["id"];
  let url = `/video/${id}`;

  const ref = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    if (ref.current) {
      ref.current.load();
    }
  }, [url]);

  return (
    <video ref={ref} controls width="100%">
      <source src={url} type="video/mp4" />
    </video>
  );
};
