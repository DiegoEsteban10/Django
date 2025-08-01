import React, { useState } from 'react';

function TodoList() {
  const [tareas, setTareas] = useState([]);
  const [nuevaTarea, setNuevaTarea] = useState('');
  const [error, setError] = useState('');

  const agregarTarea = () => {
    if (nuevaTarea.trim() === '') {
      setError('⚠️ No puedes agregar una tarea vacía.');
      return;
    }

    const nueva = {
      id: Date.now(),
      texto: nuevaTarea,
      completada: false
    };

    setTareas([...tareas, nueva]);
    setNuevaTarea('');
    setError('');
  };

  const toggleCompletada = (id) => {
    setTareas(
      tareas.map((tarea) =>
        tarea.id === id ? { ...tarea, completada: !tarea.completada } : tarea
      )
    );
  };

  const eliminarTarea = (id) => {
    setTareas(tareas.filter((tarea) => tarea.id !== id));
  };

  const tareasPendientes = tareas.filter((tarea) => !tarea.completada).length;

  return (
    <div style={{ maxWidth: '400px', margin: 'auto', textAlign: 'center' }}>
      <h2>Lista de Tareas</h2>

      <input
        type="text"
        placeholder="Escribe una tarea..."
        value={nuevaTarea}
        onChange={(e) => setNuevaTarea(e.target.value)}
      />
      <button onClick={agregarTarea} disabled={!nuevaTarea.trim()}>
        Agregar
      </button>

      {error && <p style={{ color: 'red' }}>{error}</p>}

      {tareas.length === 0 ? (
        <p><strong>No tienes tareas pendientes</strong></p>
      ) : (
        <ul style={{ listStyle: 'none', padding: 0 }}>
          {tareas.map((tarea) => (
            <li
              key={tarea.id}
              style={{
                margin: '10px 0',
                textDecoration: tarea.completada ? 'line-through' : 'none',
                color: tarea.completada ? 'gray' : 'black',
              }}
            >
              {tarea.texto}
              <button onClick={() => toggleCompletada(tarea.id)} style={{ marginLeft: '10px' }}>
                ✅
              </button>
              <button onClick={() => eliminarTarea(tarea.id)} style={{ marginLeft: '5px' }}>
                🗑️
              </button>
            </li>
          ))}
        </ul>
      )}

      <p>Tareas pendientes: {tareasPendientes}</p>
    </div>
  );
}

export default TodoList;
    