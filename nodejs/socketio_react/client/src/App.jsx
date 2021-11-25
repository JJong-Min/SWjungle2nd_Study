import { useState } from "react";
import "./App.css"
import Card from "./components/card/Card"
import Navbar from "./components/navbar/Navbar"
const App = () => {
  const [username, setUsername] = useState("")
  const [user, setUser] = useState("")
  
  console.log(user);
  return <div className="container">
    {user ? (
      <>
        <Navbar/>
        <Card/>
        <span className="username">{username}</span>
      </>
    ) :(
    <div className="login">
      <input 
        type="text"  
        placeholder="username" 
        onChange={(e) => setUsername(e.target.value)}/>
      <button onClick={() => setUser(username)}>login</button>
    </div>
  )}
  </div>;
}

export default App;
