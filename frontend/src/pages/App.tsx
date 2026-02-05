import Dashboard from "../components/Dashboard";
import Header from "../components/Header";
import MemoryPanel from "../components/MemoryPanel";
import ProactivePanel from "../components/ProactivePanel";
import "./App.css";

const App = () => {
  return (
    <div className="app-shell">
      <Header />
      <main className="app-content">
        <section className="app-left">
          <Dashboard />
          <MemoryPanel />
        </section>
        <section className="app-right">
          <ProactivePanel />
        </section>
      </main>
    </div>
  );
};

export default App;
