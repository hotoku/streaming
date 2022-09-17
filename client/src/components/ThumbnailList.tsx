import { Video } from "../types/Video";

const makeElement = (v: Video): JSX.Element => {
  const url = v.thumbnail_path;
  return <img src={url} key={v.id} alt="thumbnail" />;
};

export const ThumbnailList = (props: { vs: Video[] }): JSX.Element => {
  return <div>{props.vs.map(makeElement)}</div>;
};
