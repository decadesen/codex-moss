import { Memory } from "../services/api";
import "./MemoryPanel.css";

type MemoryPanelProps = {
  memories: Memory[];
};

const MemoryPanel = ({ memories }: MemoryPanelProps) => {
  return (
    <section className="card memory-panel">
      <h2>记忆上下文精选</h2>
      <ul>
        {memories.length === 0 ? (
          <li>暂无记忆数据，请先在后端创建记忆条目。</li>
        ) : (
          memories.slice(0, 3).map((memory) => (
            <li key={memory.id}>
              <span>{memory.type}：</span>
              {memory.content}
            </li>
          ))
        )}
      </ul>
    </section>
  );
};

export default MemoryPanel;
