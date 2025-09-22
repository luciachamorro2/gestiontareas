import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000", // URL de tu backend
});

export const getTasks = () => api.get("/tasks");
export const getUsers = () => api.get("/users");
