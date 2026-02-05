import "./MemoryPanel.css";

const MemoryPanel = () => {
  return (
    <section className="card memory-panel">
      <h2>记忆上下文精选</h2>
      <ul>
        <li>
          <span>长期目标：</span>完成 12 周英语口语计划，已进入第 4 周。
        </li>
        <li>
          <span>行为偏好：</span>晨间深度工作效率最高，下午适合复盘。
        </li>
        <li>
          <span>近期事件：</span>本周三有学习复盘，需要准备问题清单。
        </li>
      </ul>
    </section>
  );
};

export default MemoryPanel;
