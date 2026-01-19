import axiosPrivate from "./axiosPrivate";

export const getLeads = () => axiosPrivate.get("leads/");

export const createLead = async (data) => {
    try {
        const res = await axiosPrivate.post("leads/", data);
        return { success: true, data: res.data };
    } catch (err) {
        return {
            success: false,
            error:
                err.response?.data?.email?.[0] ||
                err.response?.data?.non_field_errors?.[0] ||
                "Failed to create lead",
        };
    }
};

export const updateLead = (id, data) =>
    axiosPrivate.patch(`leads/${id}/`, data);

export const deleteLead = (id) =>
    axiosPrivate.delete(`leads/${id}/`);

export const convertLead = (id) =>
    axiosPrivate.post(`leads/${id}/convert/`);
