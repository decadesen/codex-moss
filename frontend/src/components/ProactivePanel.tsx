import "./ProactivePanel.css";

const ProactivePanel = () => {
  return (
    <section className="card proactive-panel">
      <h2>主动对话中心</h2>
      <div className="proactive-item">
        <p className="title">学习计划到期提醒</p>
        <p className="description">
          你的「英语口语 12 周计划」本周需要完成 3 次练习。
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
