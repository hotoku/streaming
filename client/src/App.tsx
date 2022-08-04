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
  const [isSending, setIsSending] = useState<boolean>(false);

  useEffect(() => {
    const request = async () => {
      if (isSending) return;
      setIsSending(true);

      const data = await fetchVideos();

      console.log(data);
    };
    request().catch(console.error);
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
