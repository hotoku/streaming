import { Link } from "react-router-dom";
import { Video } from "../types/Video";

const makeElement = (v: Video): JSX.Element => {
  const turl = `/thumbnail/${v.id}?path=${v.thumbnail_path}`;
  const path = window.btoa(v.video_path);
  const link = `/play/${v.id}/path/${path}`;
  console.log(path);
  return (
    <Link to={link} key={v.id}>
      <img src={turl} alt="thumbnail" />
    </Link>
  );
};

export const ThumbnailList = (props: { vs: Video[] }): JSX.Element => {
  return <div>{props.vs.map(makeElement)}</div>;
};
