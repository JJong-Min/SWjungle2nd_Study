const schedule = require("node-schedule");

// 생명체 사망 api and 졸업 api
exports.j = schedule.scheduleJob({ hour: 21, minute: 31 }, function () {
    let today = new Date();
    let day = today.getDay();
    console.log(day);
});
    /*
    connection.query(
      "INSERT INTO Alien_dead(id, user_info_id, Challenge_id, createDate, alienName, color, accuredAuthCnt, failureCnt, life, graduate_toggle, week_auth_cnt, total_auth_cnt, auth_day) SELECT id, user_info_id, Challenge_id, createDate, alienName, color, accuredAuthCnt, failureCnt, life, graduate_toggle, week_auth_cnt, total_auth_cnt, auth_day FROM Alien where week_auth_cnt < total_auth_cnt AND (auth_day = 7 OR auth_day = ?)",
      [day],
      function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success insert dead_alien!!!!!!!!!", results);
      }
    );
    connection.query(
      "INSERT INTO dead_authentification SELECT Authentification.id, Authentification.user_info_id, Alien_id, Authentification.Challenge_id, requestDate, responseDate, requestUserNickname, responseUserNickname, isAuth, imgURL, comment FROM Authentification LEFT JOIN Alien ON Alien.id = Authentification.Alien_id where week_auth_cnt < total_auth_cnt AND (auth_day = 7 OR auth_day = ?)",
      [day],
      function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success insert dead_authentification!!!!!!!!!", results);
      }
    );
    connection.query(
      "DELETE FROM Authentification USING Alien LEFT JOIN Authentification ON Alien.id = Authentification.Alien_id where week_auth_cnt < total_auth_cnt AND (auth_day = 7 OR auth_day = ?)",
      [day],
      function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success delete authentification!!!!!!!!!", results);
      }
    );
    connection.query(
      "DELETE FROM Alien where week_auth_cnt < total_auth_cnt AND (auth_day = 7 OR auth_day = ?)",
      [day],
      function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success delete Alien!!!!!!!!!", results);
      }
    );
    connection.query(
      "UPDATE Alien SET week_auth_cnt = 0 where auth_day = 7 OR auth_day = ?",
      [day],
      function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success update Alien!!!!!!!!!", results);
      }
    );
    // week_auth_cnt != total_auth_cnt을 이용해서 중복으로 빼주는 것 방지하기
    connection.query(
      'UPDATE Challenge challenge, Alien_dead alien SET challenge.participantNumber = challenge.participantNumber - 1 WHERE challenge.id = alien.Challenge_id AND  alien.week_auth_cnt != alien.total_auth_cnt'
      , function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success update challenge pariticipant_number!!!!!!");
      }
    );
    // user_info_has_challenge table row 삭제
    connection.query(
      'SELECT COUNT(*) FROM Challenge challenge, Alien_dead alien WHERE challenge.id = alien.Challenge_id AND alien.week_auth_cnt != alien.total_auth_cnt', function(err, results) {
          connection.query('UPDATE ')
      });
      'DELETE FROM user_info_has_Challenge USING Alien_dead LEFT JOIN user_info_has_Challenge ON Alien_dead.Challenge_id = user_info_has_Challenge.Challenge_id where week_auth_cnt != total_auth_cnt'
      , function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success update alien_dead colum 0!!!!!!");
      }
    );
    // week_auth_cnt = total_auth_cnt으로 변경
    connection.query(
      'UPDATE Alien_dead SET week_auth_cnt = total_auth_cnt WHERE week_auth_cnt != total_auth_cnt'
      , function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success update alien_dead colum 0!!!!!!");
      }
    );
    
  
    // 졸업 API
    connection.query(
      "INSERT INTO Alien_graduated(id, user_info_id, Challenge_id, createDate, alienName, color, accuredAuthCnt, failureCnt, life, graduate_toggle, week_auth_cnt, total_auth_cnt, auth_day) SELECT id, user_info_id, Challenge_id, createDate, alienName, color, accuredAuthCnt, failureCnt, life, graduate_toggle, week_auth_cnt, total_auth_cnt, auth_day FROM Alien where graduate_toggle = 1 AND (auth_day = 7 OR auth_day = ?)",
      [day],
      function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success insert graduated_alien!!!!!!!!!", results);
      }
    );
    connection.query(
      "INSERT INTO graduated_authentification SELECT Authentification.id, Authentification.user_info_id, Alien_id, Authentification.Challenge_id, requestDate, responseDate, requestUserNickname, responseUserNickname, isAuth, imgURL, comment FROM Authentification LEFT JOIN Alien ON Alien.id = Authentification.Alien_id where graduate_toggle = 1 AND (auth_day = 7 OR auth_day = ?)",
      [day],
      function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log(
          "success insert graduated_authentification!!!!!!!!!",
          results
        );
      }
    );
    connection.query(
      "DELETE FROM Authentification USING Alien LEFT JOIN Authentification ON Alien.id = Authentification.Alien_id where graduate_toggle = 1 AND (auth_day = 7 OR auth_day = ?)",
      [day],
      function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success delete authentification!!!!!!!!!", results);
      }
    );
    connection.query(
      "DELETE FROM Alien where graduate_toggle = 1 AND (auth_day = 7 OR auth_day = ?)",
      [day],
      function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success delete Alien!!!!!!!!!", results);
      }
    );
    connection.query(
      'UPDATE Challenge challenge, Alien_graduated alien SET challenge.participantNumber = challenge.participantNumber - 1 WHERE challenge.id = alien.Challenge_id;',
      [req.challenge_id],
      function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success update challenge pariticipant_number!!!!!!");
      }
    );
    // alien_graduated에 column 추가(is_subtract)해서 중복으로 빼주는 것 방지하기
    connection.query(
      'UPDATE Challenge challenge, Alien_graduated alien SET challenge.participantNumber = challenge.participantNumber - 1 WHERE challenge.id = alien.Challenge_id AND alien.is_subtract = 1'
      , function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success update challenge pariticipant_number!!!!!!");
      }
    );
    // alien_graduated에 column(is_subtract) 0으로 변경
    connection.query(
      'UPDATE Alien_graduated SET is_subtract = 0 where is_subtract = 1'
      , function (err, results) {
        if (err) {
          console.error(err);
        }
        console.log("success update alien_dead colum 0!!!!!!");
      }
    );
    // user_info_has_challenge table row 삭제
  });
  */