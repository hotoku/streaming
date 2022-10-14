import { Routes, Route, Link, BrowserRouter } from "react-router-dom";
import { RecoilRoot } from "recoil";
import { Header } from "./Header";
import ErrorBoundary from "./ErrorBoundary";
import { Home } from "./Home";
import { Play } from "./Play";

export const App = (): JSX.Element => {
  return (
    <RecoilRoot>
      <ErrorBoundary>
        <Header />
        <BrowserRouter>
          <Routes>
            <Route index element={<Home />} />
            <Route path="/play/:id" element={<Play />} />
            <Route path="/play/:id/path/:path" element={<Play />} />
            <Route path="*" element={<NoMatch />} />
          </Routes>
        </BrowserRouter>
      </ErrorBoundary>
    </RecoilRoot>
  );
};

const NoMatch = (): JSX.Element => {
  return (
    <div>
      <h2>Nothing to see here!</h2>
      <p>
        <Link to="/">Go to the home page</Link>
      </p>
    </div>
  );
};
