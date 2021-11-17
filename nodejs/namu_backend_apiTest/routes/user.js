const express = require("express");
const router = express.Router();
const bcrypt = require("bcrypt");

var isOwner = (req, res) => {
  if (req.user) {
    return true;
  } else {
    return false;
  }
};

module.exports = function (passport, connection) {
  router.get("/:userId", (req, res) => {
    const user_id = req.params.userId;
    try {
    connection.query('(SELECT * FROM Alien JOIN Challenge ON Challenge.id = Alien.Challenge_id WHERE Alien.user_info_id = ?) UNION (SELECT * FROM Alien_graduated JOIN Challenge ON Challenge.id = Alien_graduated.Challenge_id WHERE Alien_graduated.user_info_id = ?)', [user_id, user_id], function(err, result) {
      res.status(200).json({
        result: "success",
        data: result,
        });
    })
  } catch (err) {
    console.error(err);
    res.status(501).json({
      result: "fail",
      msg: "cant select infomations"
    });  
  }
  });
 

  router.use(function (req, res, next) {
    res.status(404).send("Sorry cant find that!");
  });

  router.use(function (err, req, res, next) {
    console.error(err.stack);
    res.status(500).send("Something broke!");
  });

  return router;
}