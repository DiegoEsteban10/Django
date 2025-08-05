import { FaTrash } from 'react-icons/fa';

const Contacto = ({ contacto, onEliminar }) => {
  return (
    <li className="contacto">
      <div>
        <strong>{contacto.nombre}</strong> - {contacto.correo}
      </div>
      <button onClick={() => onEliminar(contacto)}>
        <FaTrash />
      </button>
    </li>
  );
};

export default Contacto;
