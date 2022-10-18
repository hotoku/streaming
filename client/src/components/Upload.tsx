import { useCallback, useState } from "react";
import { blobToBase64 } from "../utils";

const chunkSize = 1024 * 1024;

class Counter {
  num: number;
  constructor() {
    this.num = 0;
  }
  increment = () => {
    this.num += 1;
  };
  reset = () => {
    this.num = 0;
  };
}

const Upload = (): JSX.Element => {
  const [file, setFile] = useState<File | undefined>();
  const [sending, setSending] = useState(false);
  const [numTotalChunk, setNumTotalChunk] = useState(0);
  const [numSent, setNumSent] = useState<number>(0);

  const sendChunk = async (
    chunk: Blob,
    name: string,
    num: number
  ): Promise<void> => {
    const b64 = await blobToBase64(chunk);
    const data = new FormData();
    data.append("name", `${name}-${num}`);
    data.append("content", b64);
    const options = {
      method: "POST",
      body: data,
    };
    const ret = await fetch(`/upload?num=${num}`, options);
    console.log(`finish ${num}, ${numSent}`);
    setNumSent(numSent + 1);
  };

  const sendFile = async () => {
    if (!file) {
      return;
    }
    setSending(true);
    const numChunk = Math.ceil(file.size / chunkSize);
    setNumTotalChunk(numChunk);

    const pros = [] as Promise<void>[];
    for (let i: number = 0; i < numChunk; i++) {
      const chunk = file.slice(i * chunkSize, (i + 1) * chunkSize);
      pros.push(sendChunk(chunk, file.name, i));
    }
    await Promise.all(pros);
  };

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
      {sending ? (
        <div>
          sending {numSent} / {numTotalChunk}
        </div>
      ) : null}
    </div>
  );
};

export default Upload;
