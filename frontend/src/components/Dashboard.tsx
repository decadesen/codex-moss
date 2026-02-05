import "./Dashboard.css";

const Dashboard = () => {
  return (
    <section className="card">
      <h2>今日概览</h2>
      <div className="dashboard-grid">
        <div>
          <p className="label">主动提醒</p>
          <p className="value">3 条待处理</p>
        </div>
        <div>
          <p className="label">成长计划</p>
          <p className="value">2 项进行中</p>
        </div>
        <div>
          <p className="label">情绪状态</p>
          <p className="value">专注度偏高</p>
        </div>
        <div>
          <p className="label">记忆更新</p>
          <p className="value">5 条高可信度</p>
        </div>
      </div>
    </section>
  );
};

export default Dashboard;
