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
export const createUser = (userData) => axios.post(`${API_URL}/users`, userData);
export const updateUser = (userId, userData) => 
  axios.put(`${API_URL}/users/${userId}`, userData);
export const deleteUser = (id) => {
  return axios.delete(`${API_URL}/users/${id}`);
};