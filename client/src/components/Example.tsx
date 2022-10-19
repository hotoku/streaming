import { useState } from "react";

const task = (n: number): Promise<void> =>
  new Promise((resolve) => setTimeout(resolve, n * 1000));

const Example = (): JSX.Element => {
  const [num, setNum] = useState(0);

  const runTask = async (n: number): Promise<void> => {
    await task(n);
    console.log("done task", n);
    setNum((n) => n + 1);
  };

  return (
    <div>
      <button
        onClick={async () => {
          const tasks = [] as Promise<void>[];
          for (let i = 1; i <= 3; i++) {
            tasks.push(runTask(i));
          }
          await Promise.all(tasks);
          console.log("done all task");
        }}
      >
        start
      </button>
      <p>num={num}</p>
    </div>
  );
};

export default Example;
