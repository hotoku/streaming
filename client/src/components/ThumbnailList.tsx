import { Video } from "../types/Video";

const makeElement = (v: Video): JSX.Element => {
  return <img src={v.thumbnail_path} key={v.id} />;
};

export const ThumbnailList = (props: { vs: Video[] }): JSX.Element => {
  return <div>{props.vs.map(makeElement)}</div>;
};
