# 系统架构与技术假设

## 1. 逻辑架构
- **前端**：多端（Web/移动端）对话界面与个人档案管理
- **后端**：对话编排、记忆管理、计划/教练模块、事件触发
- **AI 核心**：LLM + 记忆/检索系统 + 策略引擎
- **数据层**：关系型数据库 + 向量检索存储
- **集成层**：第三方工具与插件

## 2. 关键模块
- **Conversation Orchestrator**：对话与上下文协调
- **Memory Engine**：记忆存储与召回
- **Coach Engine**：目标与成长反馈
- **Trigger Engine**：主动对话与提醒
- **External Connector**：外部数据接入

## 3. 技术假设（可选）
> 仅作为实现参考，可替换
- 前端：React / Vue
- 后端：Node.js / Python FastAPI
- 数据库：PostgreSQL
- 向量检索：pgvector / Milvus
- 消息通知：短信/邮件/IM

## 4. 多模态扩展
保留对语音/图像/传感器接入的接口设计，但不作为当前必交付范围。
