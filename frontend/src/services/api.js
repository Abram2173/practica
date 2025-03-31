import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000", // Cambia a tu backend
});

export const login = async (username, password) => {
  const response = await api.post("/auth/login", { username, password });
  return response.data;
};

export const register = async (userData, token) => {
  const response = await api.post("/auth/register", userData, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });
  return response.data;
};
