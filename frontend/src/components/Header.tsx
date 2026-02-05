import "./Header.css";

const Header = () => {
  return (
    <header className="header">
      <div>
        <p className="header-title">MOSS 个人智能助理</p>
        <p className="header-subtitle">
          长期记忆 · 主动沟通 · 成长教练 · 多模态扩展
        </p>
      </div>
      <button className="header-button">进入专注模式</button>
    </header>
  );
};

export default Header;
