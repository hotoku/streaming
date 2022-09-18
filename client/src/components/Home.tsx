import "./App.css";
import { useEffect } from "react";
import { ThumbnailList } from "../components/ThumbnailList";
import { fetchVideoList } from "../db";
import { useRecoilState } from "recoil";
import { videoListAtom } from "../atoms";

export const Home = () => {
  const [videoList, setVideoList] = useRecoilState(videoListAtom);
  useEffect(() => {
    if (videoList.length <= 0) {
      console.log("new list");
      fetchVideoList(setVideoList);
    }
  }, []);
  return ThumbnailList({ vs: videoList });
};
