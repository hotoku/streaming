import { useCallback, useState } from "react";
import { fileToBase64 } from "../utils";

type Options = {
  method: "POST";
  body: any;
  headers: {
    "Content-Type"?: string;
  };
};

const Upload = (): JSX.Element => {
  const [file, setFile] = useState<File | undefined>();

  const sendFile = useCallback(async () => {
    if (!file) {
      return;
    }
    const content = await fileToBase64(file);

    const data = new FormData();
    data.append("name", file.name);
    data.append("content", content);

    const options: Options = {
      method: "POST",
      body: data,
      headers: {
        "Content-Type": "multipart/form-data",
      },
    };
    delete options.headers["Content-Type"];

    await fetch("/upload", options);
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
    </div>
  );
};

export default Upload;
