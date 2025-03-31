import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import { FaUserPlus, FaUpload, FaChartBar } from "react-icons/fa";

function DashboardPage() {
  const [role, setRole] = useState(localStorage.getItem("role") || "operator");
  const navigate = useNavigate();

  useEffect(() => {
    // Verifica si el token de sesión es válido y establece el rol del usuario
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/login");
    }
  }, [navigate]);

  return (
    <div className="min-h-screen bg-gray-100 font-sans">
      <header className="bg-blue-800 text-white py-4">
        <div className="container mx-auto px-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold">Dashboard - {role}</h1>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {role === "admin" && (
            <button
              className="bg-green-600 text-white px-6 py-3 rounded-lg flex items-center justify-center hover:bg-green-700"
            >
              <FaUserPlus className="mr-2" /> Aprobar/Registrar Usuarios
            </button>
          )}
          {(role === "operator" || role === "admin") && (
            <button
              className="bg-blue-600 text-white px-6 py-3 rounded-lg flex items-center justify-center hover:bg-blue-700"
            >
              <FaUpload className="mr-2" /> Subir Inspección
            </button>
          )}
          {(role === "inspector" || role === "admin") && (
            <button
              className="bg-purple-600 text-white px-6 py-3 rounded-lg flex items-center justify-center hover:bg-purple-700"
            >
              <FaChartBar className="mr-2" /> Ver Resultados
            </button>
          )}
        </div>
      </main>
    </div>
  );
}

export default DashboardPage;
