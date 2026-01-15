import api from "./axios";
export const getDeals = () => api.get("deals/");
export const updateStage = (id, stage) => {
    return api.patch(`/deals/${id}/stage/`, {
        stage: stage,
    });
};
