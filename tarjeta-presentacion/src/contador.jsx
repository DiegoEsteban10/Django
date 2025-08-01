import { useState } from "react";
function Contador() {
    const [Contador,setContador] = useState(0)
    return (
        <div style={{textAlign:"center"}}>
            <h2>Contador</h2> 
            <p>clicks: {Contador}</p>
            <button>onClick = {() => setContador(Contador + 1)} +</button>
            <button>onClick = {() => setContador(Contador - 1)} -</button>          
            <button>reset = {() => setContador(0)}</button>          

        </div>
    )
}

export default Contador