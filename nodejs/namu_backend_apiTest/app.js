const path = require("path");
const dotenv = require("dotenv");
dotenv.config({ path: path.join(__dirname, "../.env") });
const mysql = require("mysql");
const express = require("express");
const morgan = require("morgan");
const app = express();
const scheduler = require("./routes/scheduler.js");


const port = process.env.PORT || 5000;

app.listen(port, () => {
  console.log(`** Raising Alien Creatures Web Server **`);
  console.log(`App listening on port ${port}`);
});
