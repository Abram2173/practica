import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { register } from "../services/api";

function RegisterPage() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [role, setRole] = useState("operator");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      const userData = { username, email, role, password };
      await register(userData);
      setMessage("Usuario registrado con éxito. Esperando aprobación.");
      navigate("/dashboard"); // Redirige a dashboard o página de éxito
    } catch (error) {
      setMessage("Error al registrar el usuario.");
    }
  };

  return (
    <div className="min-h-screen flex items-center justify-center">
      <form onSubmit={handleRegister} className="bg-white p-6 rounded-md shadow-md">
        <h2 className="text-2xl font-bold mb-4">Registrar Usuario</h2>
        <div>
          <label className="block text-sm">Username</label>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            className="border w-full p-2 rounded-md"
          />
        </div>
        <div className="mt-4">
          <label className="block text-sm">Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="border w-full p-2 rounded-md"
          />
        </div>
        <div className="mt-4">
          <label className="block text-sm">Role</label>
          <select
            value={role}
            onChange={(e) => setRole(e.target.value)}
            className="border w-full p-2 rounded-md"
          >
            <option value="operator">Operador</option>
            <option value="inspector">Inspector</option>
          </select>
        </div>
        <div className="mt-4">
          <label className="block text-sm">Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="border w-full p-2 rounded-md"
          />
        </div>
        <button type="submit" className="mt-4 bg-blue-600 text-white p-2 w-full rounded-md">
          Registrar Usuario
        </button>
        {message && <p className="text-red-600 mt-2">{message}</p>}
      </form>
    </div>
  );
}

export default RegisterPage;
