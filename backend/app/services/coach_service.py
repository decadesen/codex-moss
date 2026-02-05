from sqlalchemy.orm import Session

from app.models.goal import Goal
from app.schemas.coach import CoachSummary
from app.services.memory_service import retrieve_memories_with_scores


def build_coach_summary(db: Session) -> CoachSummary:
    active_goals = (
        db.query(Goal)
        .filter(Goal.status == "active")
        .order_by(Goal.progress.asc(), Goal.id.desc())
        .all()
    )
    memories = retrieve_memories_with_scores(db, limit=5)
    focus = active_goals[0].title if active_goals else "暂无进行中的目标"
    observations = []
    if active_goals:
        observations.append(f"当前进行中目标 {len(active_goals)} 项，需要持续跟进。")
        slow_goals = [goal for goal in active_goals if goal.progress < 0.4]
        if slow_goals:
            observations.append("部分目标进度偏慢，可考虑拆分小步骤。")
    if memories:
        observations.append("近期记忆中有高相关信息，可用于调整行动计划。")
    suggested_actions = []
    if active_goals:
        suggested_actions.append(f"为「{active_goals[0].title}」安排下一次行动。")
    if memories:
        suggested_actions.append("复盘最近 3 条记忆，提炼可执行要点。")
    related_memories = [memory.content for memory, _, _ in memories[:3]]
    return CoachSummary(
        focus=focus,
        observations=observations,
        suggested_actions=suggested_actions,
        related_memories=related_memories,
    )
