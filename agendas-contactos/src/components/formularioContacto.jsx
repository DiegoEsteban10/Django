import { useState } from 'react';
import { FaUser, FaEnvelope } from 'react-icons/fa';

const FormularioContacto = ({ agregarContacto }) => {
  const [nombre, setNombre] = useState('');
  const [correo, setCorreo] = useState('');
  const [error, setError] = useState('');

  const manejarSubmit = (e) => {
    e.preventDefault();

    if (nombre.trim() === '' || correo.trim() === '') {
      setError('Todos los campos son obligatorios');
      return;
    }

    setError('');
    agregarContacto({ nombre, correo });
    setNombre('');
    setCorreo('');
  };

  return (
    <form className="formulario-contacto" onSubmit={manejarSubmit}>
      <label>
        <FaUser style={{ marginRight: '8px' }} />
        Nombre:
      </label>
      <input
        type="text"
        value={nombre}
        onChange={(e) => setNombre(e.target.value)}
        placeholder="Ingresa un nombre"
      />

      <label>
        <FaEnvelope style={{ marginRight: '8px' }} />
        Correo:
      </label>
      <input
        type="email"
        value={correo}
        onChange={(e) => setCorreo(e.target.value)}
        placeholder="correo@ejemplo.com"
      />

      <button type="submit">Agregar contacto</button>
    </form>
  );
};

export default FormularioContacto;
