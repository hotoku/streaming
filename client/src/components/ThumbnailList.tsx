import { Video } from "../types/Video";

const makeElement = (v: Video): JSX.Element => {
  const vurl = `/video/${v.id}?path=${v.video_path}`;
  const turl = `/thumbnail/${v.id}?path=${v.thumbnail_path}`;
  return (
    <a key={v.id} href={vurl}>
      <img src={turl} alt="thumbnail" />
    </a>
  );
};

export const ThumbnailList = (props: { vs: Video[] }): JSX.Element => {
  return <div>{props.vs.map(makeElement)}</div>;
};
