import "./App.css";
import { useEffect, useState } from "react";
import { Video } from "../types/Video";
import { ThumbnailList } from "../components/ThumbnailList";
import { fetchVideoList } from "../db";

export const Home = () => {
  const [videos, setVideos] = useState<Video[]>([]);
  useEffect(() => {
    if (videos.length <= 0) {
      console.log("new list");
      fetchVideoList(setVideos);
    }
  }, []);
  return ThumbnailList({ vs: videos });
};
