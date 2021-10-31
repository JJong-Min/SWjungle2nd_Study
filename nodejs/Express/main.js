const express = require('express');
const logger = require('morgan');
const app = express();

app.use(logger('dev'));
app.listen(3000, () => console.log('running'));