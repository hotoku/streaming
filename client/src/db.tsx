import { Video } from "./types/Video";

export const fetchVideoList = async (setVideos: (vs: Video[]) => void) => {
  const response = await fetch("/video/list");
  const data = await response.json();
  console.log(data);
  setVideos(data);
};
