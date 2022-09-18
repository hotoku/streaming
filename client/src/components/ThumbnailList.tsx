import { Link } from "react-router-dom";
import { Video } from "../types/Video";

const makeUrl = (id: number, path: string): string => {
  try {
    const encoded = window.btoa(path);
    return `/play/${id}/path/${encoded}`;
  } catch (error: any) {
    return `/play/${id}`;
  }
};

const makeElement = (v: Video): JSX.Element => {
  const turl = `/thumbnail/${v.id}?path=${v.thumbnail_path}`;
  const link = makeUrl(v.id, v.video_path);
  return (
    <Link to={link} key={v.id}>
      <img src={turl} alt="thumbnail" />
    </Link>
  );
};

export const ThumbnailList = (props: { vs: Video[] }): JSX.Element => {
  return <div>{props.vs.map(makeElement)}</div>;
};
