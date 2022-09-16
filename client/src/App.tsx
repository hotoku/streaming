import "./App.css";
import { useEffect, useState } from "react";

interface Video {
  video_path: string;
  thumbnail_path: string;
  id: number;
}

const makeElement = (v: Video) => {
  return (
    <div>
      {v.video_path}, {v.thumbnail_path}, {v.id}
    </div>
  );
};

const fetchVideoList = (setVideos: any) => {
  return 1;
};

const App = () => {
  const [videos, setVideos] = useState<Video[]>([]);
  useEffect(() => {
    setVideos([
      {
        video_path: "a",
        thumbnail_path: "b",
        id: 1,
      },
    ]);
    fetchVideoList(1);
  });
  return <div>{videos.map(makeElement)}</div>;
};

export default App;
