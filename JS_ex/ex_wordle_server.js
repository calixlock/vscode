const express = require('express');
const app = express();
app.listen(8080, function(){
    console.log('listening on 8080')
}); // listen(서버를 띄울 포트번호 , 띄운 후 실행할 코드)


app.get('/',function(req,res){
    res.sendFile(__dirname + '/ex_wordle.html')
});