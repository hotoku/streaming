import logo from "./logo.svg";
import "./App.css";
import { useEffect, useState } from "react";

type Video = {
  id: number;
  name: string;
};
type VideosResponse = Video[];

const fetchVideos = async (): Promise<VideosResponse> => {
  const resp = await fetch("/videos", {
    method: "get",
  });
  const data: VideosResponse = await resp.json();
  return data;
};

function App() {
  const [videos, setVideos] = useState<Video[]>([]);
  const [isSending, setIsSending] = useState<boolean>(false);

  useEffect(() => {
    const request = async () => {
      if (isSending) return;
      setIsSending(true);

      const data = await fetchVideos();
      setVideos(data);

      console.log(data);
    };
    request().catch(console.error);
  }, []);

  return (
    <div className="App">
      <header className="App-header">ヘッダー</header>
      <div className="App-contents">
        <ul>
          {videos.map((v) => {
            return <li key={v.id}>{v.name}</li>;
          })}
        </ul>
      </div>
      <footer className="App-footer">フッター</footer>
    </div>
  );
}

export default App;
