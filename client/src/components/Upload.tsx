import { read } from "fs";

type Options = {
  method: "POST";
  body: any;
  headers: {
    "Content-Type"?: string;
  };
};

const Upload = (): JSX.Element => {
  return (
    <div>
      <input
        type="file"
        multiple
        id="hoge"
        onChange={(e) => {
          const files = e.target.files;
          if (files === null) return;
          const file = files[0];
          const reader = new FileReader();
          reader.onload = () => {
            console.log(typeof reader.result);
            console.log(reader.result);
          };

          // reader.readAsBinaryString(file);
          reader.readAsArrayBuffer(file);

          const data = new FormData();
          data.append("name", file.name);
          data.append("content", file);

          const options: Options = {
            method: "POST",
            body: data,
            headers: {
              "Content-Type": "multipart/form-data",
            },
          };
          delete options.headers["Content-Type"];

          fetch("/upload", options);
        }}
      />
      <button
        onClick={() => {
          const data = new FormData();
          data.append("name", "hoge");
          fetch("/upload", {
            method: "POST",
            body: data,
          });
        }}
      >
        push
      </button>
    </div>
  );
};

export default Upload;
