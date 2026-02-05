const API_BASE =
  import.meta.env.VITE_API_BASE ?? "http://localhost:8000/api";

export type Profile = {
  id: number;
  display_name: string;
  bio?: string | null;
  timezone: string;
};

export type Memory = {
  id: number;
  type: string;
  content: string;
  source: string;
  confidence: number;
  tags: string[];
};

export type Goal = {
  id: number;
  title: string;
  description?: string | null;
  due_date?: string | null;
  status: string;
  progress: number;
};

export type CoachSummary = {
  focus: string;
  observations: string[];
  suggested_actions: string[];
  related_memories: string[];
};

async function request<T>(path: string): Promise<T> {
  const response = await fetch(`${API_BASE}${path}`);
  if (!response.ok) {
    throw new Error(`Request failed: ${response.status}`);
  }
  return response.json() as Promise<T>;
}

export const api = {
  listProfiles: () => request<Profile[]>("/profiles/"),
  listMemories: () => request<Memory[]>("/memories/"),
  listGoals: () => request<Goal[]>("/goals/"),
  getCoachSummary: () => request<CoachSummary>("/coach/summary"),
};
