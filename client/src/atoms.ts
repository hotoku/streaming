import { atom } from "recoil";
import { Video } from "./types/Video";

export const videoListAtom = atom({
  key: "videoList",
  default: Array<Video>(),
});

export const hasListAtom = atom({
  key: "hasList",
  default: false,
});
