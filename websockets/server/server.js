const {createServer}=require('http');
const {Server}=require('socket.io');

const httpServer=createServer();
const io=new Server(httpServer,{
    cors:{
        origin:"http://localhost:5173"
    }
});

let playerScores=[]
io.on('connection',(socket)=>{
    

    socket.on('scores',(scores)=>{
        console.log(scores);
        playerScores.push({...scores,id:socket.id});
        
        socket.emit('playerScores',playerScores); 
    })
    
})

httpServer.listen(3000,()=>{
    console.log('Server is running on port 3000');
})