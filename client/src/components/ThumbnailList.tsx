import { Video } from "../types/Video";

const makeElement = (v: Video): JSX.Element => {
  const url = `/video/${v.id}?path=${v.video_path}`;
  return (
    <a key={v.id} href={url}>
      <img src={url} alt="thumbnail" />
    </a>
  );
};

export const ThumbnailList = (props: { vs: Video[] }): JSX.Element => {
  return <div>{props.vs.map(makeElement)}</div>;
};
