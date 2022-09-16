import "./App.css";
import { useEffect, useState } from "react";

interface Video {
  video_path: string;
  thumbnail_path: string;
  id: number;
}

const makeElement = (v: Video) => {
  return (
    <div key={v.id}>
      {v.video_path}, {v.thumbnail_path}, {v.id}
    </div>
  );
};

const fetchVideoList = async (setVideos: (vs: Video[]) => void) => {
  const response = await fetch("/video/list");
  const data = await response.json();
  console.log(data);
  setVideos(data);
};

const VideoList = (props: { vs: Video[] }): JSX.Element => {
  return <div />;
};

const App = () => {
  const [videos, setVideos] = useState<Video[]>([]);
  useEffect(() => {
    fetchVideoList(setVideos);
  }, []);
  return <div>{videos.map(makeElement)}</div>;
};

export default App;
