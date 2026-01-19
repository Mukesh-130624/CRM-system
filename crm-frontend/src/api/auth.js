import axiosPublic from "./axiosPublic";

export const login = (data) => axiosPublic.post("auth/login/", data);
export const register = (data) => axiosPublic.post("auth/register/", data);
