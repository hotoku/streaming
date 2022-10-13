import "./App.css";
import { useEffect, useState } from "react";
import { ThumbnailList } from "../components/ThumbnailList";
import { fetchVideoList } from "../db";
import { useRecoilState } from "recoil";
import { videoListAtom } from "../atoms";

export const Home = () => {
  const [videoList, setVideoList] = useRecoilState(videoListAtom);
  const [isError, setIsError] = useState(false);
  useEffect(() => {
    if (videoList.length <= 0) {
      fetchVideoList(setVideoList).catch(() => {
        setIsError(true);
      });
    }
  }, []);
  if (isError) {
    throw Error("something is wrong");
  }
  return ThumbnailList({ vs: videoList });
};
