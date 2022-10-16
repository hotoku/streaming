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
          fetch("/upload", {
            method: "POST",
            body: files[0],
          });
        }}
      />
    </div>
  );
};

export default Upload;
