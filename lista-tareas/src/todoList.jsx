import React, { useState } from 'react';
import './App.css';

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
        completada: false,
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

    const tareasPendientes = tareas.filter((t) => !t.completada).length;

    return (
    <div className="todo-container">
        <h2>🏠 Lista de Tareas del Hogar</h2>

        <div>
        <input
            type="text"
            placeholder="Escribe una tarea..."
            value={nuevaTarea}
            onChange={(e) => setNuevaTarea(e.target.value)}
        />
        <button onClick={agregarTarea} disabled={!nuevaTarea.trim()}>
            Agregar
        </button>
        </div>

        {error && <p className="mensaje">{error}</p>}

        {tareas.length === 0 ? (
        <p><strong>No tienes tareas pendientes</strong></p>
        ) : (
        <ul>
            {tareas.map((tarea) => (
            <li
                key={tarea.id}
                className={tarea.completada ? 'completada' : ''}
            >
                <span>{tarea.texto}</span>
                <button onClick={() => toggleCompletada(tarea.id)}>✅</button>
                <button onClick={() => eliminarTarea(tarea.id)}>🗑️</button>
            </li>
            ))}
        </ul>
        )}

        <p className="contador">Tareas pendientes: {tareasPendientes}</p>
    </div>
    );
}

export default TodoList;
