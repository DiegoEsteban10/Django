import React from 'react';
import fotos from '../src/fotos/133894695752377938.jpg'
import Contador  from './contador';

const hobbies = ["manejar, hacer deporte, jugar videojuegos"]
function App() {
  return (
    <div className="App" style={{ textAlign: "center" }}>
      <h1>Diego Esteban Sanchez Forero</h1>
      <img
      src = {fotos}
      alt="Foto de Diego" 
      width="200" 
      height="200" />

      <p>Desarrollador de Software en aprendizaje constante</p>

      <blockquote>"dia a dia, paso a paso"</blockquote>

      <h2>Hobbies</h2>
      <ul>
        {hobbies.map((hobby, index) => (
          <li key={index}>{hobby}</li>
        ))}      
      </ul>
      
      <p>Año actual: {new Date().getFullYear()}</p>
      
    </div>
  );
}

export default App;