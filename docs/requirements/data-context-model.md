# 数据与上下文模型

## 1. 数据对象概览
- **UserProfile**：用户基础信息与偏好
- **Memory**：可检索记忆单元
- **Conversation**：对话记录与上下文引用
- **Goal/Plan**：目标与计划
- **Event**：外部事件或系统触发事件
- **CoachNote**：教练反馈与复盘建议

## 2. 记忆结构建议
```json
{
  "id": "mem_123",
  "type": "preference | goal | fact | event | habit",
  "content": "用户偏好晨间深度工作",
  "source": "conversation | manual",
  "confidence": 0.86,
  "tags": ["工作习惯", "时间管理"],
  "created_at": "2025-01-01",
  "last_accessed": "2025-01-05",
  "decay_score": 0.12
}
```

## 3. 上下文构建逻辑（概念）
1. 识别当前对话意图与主题
2. 召回相关记忆（向量 + 规则）
3. 过滤与排序（时间、置信度、用户优先级）
4. 生成可解释上下文摘要

## 4. 计划与成长对象
```json
{
  "goal_id": "goal_001",
  "title": "三个月完成英语口语提升",
  "milestones": [
    {"title": "每周口语练习3次", "due": "2025-02-01"},
    {"title": "完成10次话题演讲", "due": "2025-03-01"}
  ],
  "status": "active",
  "progress": 0.4
}
```

## 5. 关键数据治理原则
- 数据最小化：只收集与目标相关的必要信息
- 可删除与可修正：用户可以纠正记忆
- 透明性：所有记忆召回理由可解释
