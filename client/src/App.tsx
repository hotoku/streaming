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
      <video controls width="250">
        <source src="/video/1" type="video/mp4" />
      </video>

      <div className="App-contents">
        <ul className="gallery">
          {videos.map((v) => {
            const name =
              typeof v.name === "string" ? v.name.substring(0, 10) : "unknown";
            return (
              <li key={v.id}>
                <div>{name}</div>
                <img
                  className="gallery-item"
                  src={`/video/image/${v.id}`}
                  alt={name}
                ></img>
              </li>
            );
          })}
        </ul>
      </div>
      <footer className="App-footer">フッター</footer>
    </div>
  );
}

export default App;
