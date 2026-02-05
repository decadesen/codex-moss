import { CoachSummary } from "../services/api";
import "./CoachPanel.css";

type CoachPanelProps = {
  summary: CoachSummary | null;
};

const CoachPanel = ({ summary }: CoachPanelProps) => {
  if (!summary) {
    return (
      <section className="card coach-panel">
        <h2>成长教练</h2>
        <p>暂无教练建议，请先完善目标与记忆。</p>
      </section>
    );
  }

  return (
    <section className="card coach-panel">
      <h2>成长教练</h2>
      <p className="coach-focus">当前聚焦：{summary.focus}</p>
      <div>
        <p className="coach-title">观察</p>
        <ul>
          {summary.observations.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
      <div>
        <p className="coach-title">建议行动</p>
        <ul>
          {summary.suggested_actions.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
      <div>
        <p className="coach-title">相关记忆</p>
        <ul>
          {summary.related_memories.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
    </section>
  );
};

export default CoachPanel;
