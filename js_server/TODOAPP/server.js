const express = require('express');
const app = express();

app.listen(8080, function(){
    console.log('listening on 8080');
}); // listen(서버를 띄울 포트번호 , 띄운 후 실행할 코드)

// 누군가 /pet 으로 방문시 
app.get('/pet',function(req,res){
    res.send('/pet으로 접속하셨습니다.');
});

// 누군가 /beauty 으로 방문시 
app.get('/beauty',function(req,res){
    res.send('/beauty로 접속하셨습니다.');
});

// 
app.get('/',function(req,res){
    res.sendFile(__dirname + '/index.html');
});
