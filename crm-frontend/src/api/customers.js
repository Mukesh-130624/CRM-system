import axiosPrivate from "./axiosPrivate";

export const getCustomers = () => axiosPrivate.get("customers/");
