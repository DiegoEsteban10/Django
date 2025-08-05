import { FaSearch } from 'react-icons/fa';

const BuscadorContactos = ({ busqueda, setBusqueda }) => {
  return (
    <div className="formulario-contacto">
      <label>
        <FaSearch style={{ marginRight: '8px' }} />
        Buscar:
      </label>
      <input
        type="text"
        placeholder="Buscar por nombre o correo"
        value={busqueda}
        onChange={(e) => setBusqueda(e.target.value)}
      />
    </div>
  );
};

export default BuscadorContactos;
