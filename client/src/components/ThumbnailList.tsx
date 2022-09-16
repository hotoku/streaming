import { Video } from "../types/Video";

const makeElement = (v: Video): JSX.Element => {
  return (
    <div key={v.id}>
      {v.video_path}, {v.thumbnail_path}, {v.id}
    </div>
  );
};

export const ThumbnailList = (props: { vs: Video[] }): JSX.Element => {
  return <div>{props.vs.map(makeElement)}</div>;
};
