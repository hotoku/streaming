import { Video } from "../types/Video";

const makeElement = (v: Video): JSX.Element => {
  const url = v.thumbnail_path.replace("resource/", "hoge/");
  console.log(url);
  return <img src={"/" + url} key={v.id} />;
};

export const ThumbnailList = (props: { vs: Video[] }): JSX.Element => {
  return <div>{props.vs.map(makeElement)}</div>;
};
