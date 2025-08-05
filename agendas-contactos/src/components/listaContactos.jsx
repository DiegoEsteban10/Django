import React from 'react';
import Contacto from './contacto';

const ListaContactos = ({ contactos, filtro, onEliminar }) => {
  const filtroLower = filtro.toLowerCase();
  
  const contactosFiltrados = contactos.filter(contacto =>
  (contacto.nombre && contacto.nombre.toLowerCase().includes(filtro.toLowerCase())) ||
  (contacto.correo && contacto.correo.toLowerCase().includes(filtro.toLowerCase()))
);


  return (
    <div className="lista-contactos">
      <h2>📋 Lista de Contactos</h2>
      {contactosFiltrados.length > 0 ? (
        <ul>
          {contactosFiltrados.map(contacto => (
            <Contacto
              key={contacto.id}
              contacto={contacto}
              onEliminar={onEliminar}
            />
          ))}
        </ul>
      ) : (
        <p>No se encontraron contactos.</p>
      )}
    </div>
  );
};

export default ListaContactos;
