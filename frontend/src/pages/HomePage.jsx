import React from "react";
import { FaCamera } from "react-icons/fa"; // Usando FaCamera como ícono
import { Link } from "react-router-dom";

function HomePage() {
  return (
    <div className="min-h-screen bg-gray-100 font-sans">
      <header className="bg-blue-800 text-white py-4">
        <div className="container mx-auto px-4 flex justify-between items-center">
          <h1 className="text-2xl font-bold">RoadGuard</h1>
          <p className="text-sm">Monitoreo vial con drones e IA</p>
        </div>
      </header>

      <main className="container mx-auto px-4 py-8 text-center">
        <FaCamera className="text-blue-600 text-8xl mx-auto mb-4" />
        <h2 className="text-3xl font-bold mb-4">Bienvenido a RoadGuard</h2>
        <p className="text-lg mb-6">
          Monitorea carreteras en tiempo real con tecnología avanzada.
        </p>
        <Link to="/login">
          <button className="bg-blue-600 text-white px-6 py-3 rounded-lg font-semibold hover:bg-blue-700">
            Iniciar Sesión
          </button>
        </Link>
      </main>
    </div>
  );
}

export default HomePage;
