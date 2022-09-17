import { Video } from "./types/Video";

export const fetchVideoList = async (callback: (vs: Video[]) => void) => {
  const response = await fetch("/video/list");
  const data: Video[] = await response.json();
  callback(data);
};
