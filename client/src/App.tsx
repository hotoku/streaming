import "./App.css";
import { useEffect, useState } from "react";
import { Video } from "./types/Video";
import { ThumbnailList } from "./components/ThumbnailList";
import { fetchVideoList } from "./db";

const App = () => {
  const [videos, setVideos] = useState<Video[]>([]);
  useEffect(() => {
    fetchVideoList(setVideos);
  }, []);
  return ThumbnailList({ vs: videos });
};

export default App;
