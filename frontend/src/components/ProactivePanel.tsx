import { Goal } from "../services/api";
import "./ProactivePanel.css";

type ProactivePanelProps = {
  goals: Goal[];
};

const ProactivePanel = ({ goals }: ProactivePanelProps) => {
  const nextGoal = goals.find((goal) => goal.status === "active") ?? goals[0];

  return (
    <section className="card proactive-panel">
      <h2>主动对话中心</h2>
      <div className="proactive-item">
        <p className="title">学习计划到期提醒</p>
        <p className="description">
          {nextGoal
            ? `你的「${nextGoal.title}」正在进行中，当前进度 ${
                Math.round(nextGoal.progress * 100) / 100
              }。`
            : "暂无计划，建议创建新的成长目标。"}
        </p>
      </div>
      <div className="proactive-item">
        <p className="title">外部世界变化</p>
        <p className="description">
          行业周报更新：AI Agent 领域新增 2 个关键开源项目。
        </p>
      </div>
      <button className="proactive-action">让我知道更多</button>
    </section>
  );
};

export default ProactivePanel;
