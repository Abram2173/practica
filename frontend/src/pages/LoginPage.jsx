import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:5000/auth/login", {
        username,
        password
      });
  
      // Guarda el token JWT en localStorage
      localStorage.setItem("access_token", response.data.access_token);
      
      // Redirige al Dashboard
      navigate("/dashboard");
    } catch (error) {
      setMessage("Credenciales incorrectas");
    }
  };
  


  return (
    <div className="min-h-screen bg-gray-100 font-sans">
      <header className="bg-blue-800 text-white py-4">
        <div className="container mx-auto px-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold">RoadGuard</h1>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        <form onSubmit={handleLogin} className="bg-white p-6 rounded-md shadow-md">
          <h2 className="text-2xl font-bold mb-4">Login</h2>
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
            <label className="block text-sm">Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              className="border w-full p-2 rounded-md"
            />
          </div>
          <button type="submit" className="mt-4 bg-blue-600 text-white p-2 w-full rounded-md">
            Iniciar Sesión
          </button>
          {message && <p className="mt-4 text-red-600">{message}</p>}
        </form>
      </main>
    </div>
  );
}

export default LoginPage;
