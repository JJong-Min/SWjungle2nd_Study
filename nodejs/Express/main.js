const express = require('express');
const app = express();

const mw = (req, res, next) => {
  console.log('mw!');
  next();
}

app.use(mw);
app.listen(3000, () => console.log('running'));