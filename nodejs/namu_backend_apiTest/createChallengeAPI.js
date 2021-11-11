const path = require('path');
const dotenv = require("dotenv");
dotenv.config({ path: path.join(__dirname, "./.env") });
//미들웨어 
var express = require('express');
var app = express();
var bodyParser = require('body-parser');
const port = 3001

app.use(bodyParser.urlencoded({ extended: false }));
var mysql = require('mysql');
const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
});

console.log(process.env.DB_NAME);
app.get('/challenge', function(req, res){
    console.log('/challenge', req.user);
    res.sendFile(__dirname+'/routes/createChallenge.html');
});

app.post('/challenge_process', function(req, res){
    console.log('req_post_content', req.body.challenge_name);
    const max_user = parseInt(req.body.max_user);
    const cnt_of_week = parseInt(req.body.cnt_of_week);
    const life = parseInt(req.body.life);
    connection.query('INSERT INTO Challenge (challengeName, challengeContent, createUserNickName, maxUserNumber, cntOfWeek, life) VALUES (?, ?, ?, ?, ?, ?)', [req.body.challenge_name, req.body.challenge_content, 'kangho', max_user, cnt_of_week, life], function(error, results){
        console.log(results);
    })
    res.status(200).json({
        msg: "success insert!",
    })

});

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`)
    console.log('연결성공');
  });
  
  