import React, { useState, useEffect } from "react";
import FormularioContacto from "./formularioContacto";
import ListaContactos from "./listaContactos";
import BuscadorContactos from "./buscadorContactos";

function AgendaApp() {
  const [contactos, setContactos] = useState([]);
  const [filtro, setFiltro] = useState("");
  const [mensaje, setMensaje] = useState("");

  useEffect(() => {
    const contactosGuardados = JSON.parse(localStorage.getItem("contactos")) || [];
    setContactos(contactosGuardados);
  }, []);

  useEffect(() => {
    localStorage.setItem("contactos", JSON.stringify(contactos));
  }, [contactos]);

  const agregarContacto = (nuevoContacto) => {
    const duplicado = contactos.some(c => c.correo === nuevoContacto.correo);
    if (duplicado) {
      alert("Ya existe un contacto con ese correo.");
      return;
    }
    const nuevosContactos = [...contactos, nuevoContacto];
    setContactos(nuevosContactos);
    setMensaje("¡Contacto agregado!");
    setTimeout(() => setMensaje(""), 3000);
  };

  const eliminarContacto = (correo) => {
    const nuevosContactos = contactos.filter(contacto => contacto.correo !== correo);
    setContactos(nuevosContactos);
    setMensaje("Contacto eliminado.");
    setTimeout(() => setMensaje(""), 3000);
  };

  const contactosFiltrados = contactos.filter(contacto =>
    contacto.nombre?.toLowerCase().includes(filtro.toLowerCase()) ||
    contacto.correo?.toLowerCase().includes(filtro.toLowerCase())
  );

  return (
    <div style={{
      maxWidth: "600px",
      margin: "auto",
      background: "#fefefe",
      borderRadius: "12px",
      boxShadow: "0 0 10px rgba(0,0,0,0.1)",
      padding: "20px",
      fontFamily: "Arial, sans-serif"
    }}>
      <h1 style={{ textAlign: "center", color: "#333" }}>Agenda de Contactos de la Familia Diego</h1>
      {mensaje && <p style={{ backgroundColor: "#d4edda", padding: "10px", borderRadius: "6px", color: "#155724" }}>{mensaje}</p>}
      <BuscadorContactos filtro={filtro} setFiltro={setFiltro} />
      <FormularioContacto agregarContacto={agregarContacto} />
      <ListaContactos contactos={contactosFiltrados} onEliminar={eliminarContacto} />
    </div>
  );
}

export default AgendaApp;

