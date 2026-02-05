import { useEffect, useState } from "react";

import CoachPanel from "../components/CoachPanel";
import Dashboard from "../components/Dashboard";
import Header from "../components/Header";
import MemoryPanel from "../components/MemoryPanel";
import ProactivePanel from "../components/ProactivePanel";
import { api, CoachSummary, Goal, Memory, Profile } from "../services/api";
import "./App.css";

const App = () => {
  const [profiles, setProfiles] = useState<Profile[]>([]);
  const [memories, setMemories] = useState<Memory[]>([]);
  const [goals, setGoals] = useState<Goal[]>([]);
  const [coachSummary, setCoachSummary] = useState<CoachSummary | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        const [profilesData, memoriesData, goalsData, coachData] = await Promise.all([
          api.listProfiles(),
          api.listMemories(),
          api.listGoals(),
          api.getCoachSummary(),
        ]);
        setProfiles(profilesData);
        setMemories(memoriesData);
        setGoals(goalsData);
        setCoachSummary(coachData);
      } catch (err) {
        setError(err instanceof Error ? err.message : "加载数据失败");
      }
    };
    loadData();
  }, []);

  return (
    <div className="app-shell">
      <Header />
      {error && <div className="error-banner">⚠️ {error}</div>}
      <main className="app-content">
        <section className="app-left">
          <Dashboard
            reminders={goals.length}
            activeGoals={goals.filter((goal) => goal.status === "active").length}
            memoryCount={memories.length}
          />
          <MemoryPanel memories={memories} />
        </section>
        <section className="app-right">
          <ProactivePanel goals={goals} />
          <CoachPanel summary={coachSummary} />
          <section className="card profile-panel">
            <h2>个人档案概览</h2>
            {profiles.length === 0 ? (
              <p>暂无档案，请先创建用户档案。</p>
            ) : (
              profiles.slice(0, 2).map((profile) => (
                <div key={profile.id} className="profile-item">
                  <p className="profile-name">{profile.display_name}</p>
                  <p className="profile-meta">
                    {profile.bio || "暂无简介"} · {profile.timezone}
                  </p>
                </div>
              ))
            )}
          </section>
        </section>
      </main>
    </div>
  );
};

export default App;
