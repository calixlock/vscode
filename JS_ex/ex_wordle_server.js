/*** 
 * 터미널에서 npm init으로 초기 설정 잡아주고 package.json으로 설치 패키지들이 자동 기록 되도록 한다.
 * 터미널에서 npm install express로 패키지 설치후 server.js 파일을 만들어 아래와 같은 내용으로 포트를 열고 실행해준다.
 * 서버 자동적용 실행 // npm install -g nodemon 설치
 * nodemon server.js 형태로 실행하여 코드 변경 시 자동 반영되도록 실행한다.  
*/ 

const express = require('express');
const app = express();
app.listen(8080, function(){
    console.log('listening on 8080')
}); // listen(서버를 띄울 포트번호 , 띄운 후 실행할 코드)


app.get('/',function(req,res){
    res.sendFile(__dirname + '/ex_wordle.html')
});