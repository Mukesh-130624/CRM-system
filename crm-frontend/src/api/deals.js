import axiosPrivate from "./axiosPrivate";

export const getDeals = () => axiosPrivate.get("deals/");

export const updateStage = (id, stage) => {
    return axiosPrivate.patch(`deals/${id}/stage/`, {
        stage,
    });
};
