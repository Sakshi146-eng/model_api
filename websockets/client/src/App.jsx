import { useState } from 'react'
import { io } from 'socket.io-client';
import { useEffect } from 'react';
import './App.css'
import { use } from 'react';

function App() {
  const [score,setScore]=useState({});

  const socket=io("localhost:3000");

  function connectSocket(){
    socket.on('connection',(socket)=>{
      console.log(socket);

      socket.on("playerScores",(playerScores)=>{
        console.log(playerScores);
      }
      )
    })
  }

  function handleInput(event){
    let {name,value}= event.target;
    
    let curObj={[name]:value};
    setScore((prev)=>({...prev,...curObj}));
  }

  function sendScore(){
    console.log(score);
    socket.emit('scores',score);


  }

  useEffect(()=>{
    connectSocket();
  },[]);
  return (
    <>
      <h1>Live Dashboard</h1>
      <input type="text" name="name" placeholder="Enter Name here" onChange={handleInput}/><br />
      <input type="number" name="score" placeholder="Enter your score here" onChange={handleInput}/><br /><br />
      <button onClick={sendScore}>Push</button>

    </>
  )
}


export default App;