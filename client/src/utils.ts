export const fileToBase64 = async (file: File): Promise<string> => {
  const buf = await readAsArrayBuffer(file);
  return arrayBufferToBase64(buf);
};

const arrayBufferToBase64 = (buffer: ArrayBuffer): string => {
  var binary = "";
  var bytes = new Uint8Array(buffer);
  var len = bytes.byteLength;
  for (var i = 0; i < len; i++) {
    binary += String.fromCharCode(bytes[i]);
  }
  return window.btoa(binary);
};

const readAsArrayBuffer = (file: File): Promise<ArrayBuffer> => {
  const reader = new FileReader();

  return new Promise<ArrayBuffer>((resolve, reject) => {
    reader.onload = () => {
      const res = reader.result;
      if (res instanceof ArrayBuffer) {
        resolve(res);
      }
    };

    reader.onerror = () => {
      reader.abort();
      reject(`file read error: ${file.name}`);
    };

    reader.readAsArrayBuffer(file);
  });
};
