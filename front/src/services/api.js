import axios from "axios";

const API_URL = "http://127.0.0.1:8000"; // URL del backend

// export function getTasks() {
//   return axios.get(`${API_URL}/tasks`);
// }

// export function getUsers() {
//   return axios.get(`${API_URL}/users`);
// }

export const getTasks = () => axios.get(`${API_URL}/tasks`);
export const getUsers = () => axios.get(`${API_URL}/users`);