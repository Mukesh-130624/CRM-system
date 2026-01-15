import api from "./axios";

export const getLeads = () => api.get("leads/");
// src/api/leads.js
export const createLead = async (data) => {
    try {
        const res = await api.post("/leads/", data);
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

export const updateLead = (id, data) => api.patch(`leads/${id}/`, data);
export const deleteLead = (id) => api.delete(`leads/${id}/`);
export const convertLead = (id) => api.post(`leads/${id}/convert/`);
