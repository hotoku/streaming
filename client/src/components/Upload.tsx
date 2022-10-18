import { useCallback, useState } from "react";
import { blobToBase64 } from "../utils";

type Options = {
  method: "POST";
  body: any;
  headers: {
    "Content-Type"?: string;
  };
};

const chunkSize = 1024 * 1024;

const sendChunk = async (
  chunk: Blob,
  name: string,
  num: number,
  onFinish: (n: number) => void
): Promise<void> => {
  const b64 = await blobToBase64(chunk);
  const data = new FormData();
  data.append("name", `${name}-${num}`);
  data.append("content", b64);
  const options: Options = {
    method: "POST",
    body: data,
    headers: {
      "Content-Type": "multipart/form-data",
    },
  };
  delete options.headers["Content-Type"];
  await fetch("/upload", options);
  onFinish(num);
};

const Upload = (): JSX.Element => {
  const [file, setFile] = useState<File | undefined>();

  const sendFile = useCallback(async () => {
    if (!file) {
      return;
    }
    console.log("sendFile");
    const numChunk = Math.ceil(file.size / chunkSize);

    for (let i: number = 0; i < numChunk; i++) {
      const chunk = file.slice(i * chunkSize, (i + 1) * chunkSize);
      await sendChunk(chunk, file.name, i, (n) => {
        console.log(`${n} done`);
      });
    }
  }, [file]);

  return (
    <div>
      <input
        type="file"
        multiple
        id="hoge"
        onChange={async (e) => {
          const files = e.target.files;
          if (files === null) return;
          setFile(files[0]);
        }}
      />
      <button onClick={sendFile}>upload</button>
      <div>
        upload機能は、進捗の表示とバックグラウンドでの実行とサーバー側で非同期処理を入れないと使い物にならないので、しばらくほっとく。
      </div>
    </div>
  );
};

export default Upload;
