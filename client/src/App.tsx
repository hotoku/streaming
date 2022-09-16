import "./App.css";
import { useEffect, useState } from "react";

interface Video {
  video_path: string;
  thumbnail_path: string;
  id: number;
}

const App = () => {
  const [videos, setVideos] = useState<Video[]>([]);
  return <div>hoge</div>;
};

export default App;
