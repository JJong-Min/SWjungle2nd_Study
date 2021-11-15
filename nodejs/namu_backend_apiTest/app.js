const path = require("path");
const dotenv = require("dotenv");
dotenv.config({ path: path.join(__dirname, "../.env") });
const mysql = require("mysql");
const express = require("express");
const morgan = require("morgan");
const app = express();


const connection = mysql.createConnection({
  host: process.env.DB_HOST,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_NAME,
  multipleStatements: true,
});
connection.connect();


app.use(morgan("dev")); // middleware for logging HTTP request

const challengeRouter = require("./routes/challenge.js")(connection);
const alienRouter = require("./routes/alien.js")(connection);

app.use("/api/challenge", challengeRouter);
app.use("/api/alien", alienRouter);



const port = process.env.PORT || 5000;

app.listen(port, () => {
  console.log(`** Raising Alien Creatures Web Server **`);
  console.log(`App listening on port ${port}`);
  console.log(`DB_NAME: ${process.env.DB_NAME}`);
});
