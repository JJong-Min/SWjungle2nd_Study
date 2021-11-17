const schedule = require("node-schedule");

exports.j = schedule.scheduleJob({ hour: 21, minute: 25 }, function () {
    let today = new Date();
    let day = today.getDay();
    console.log(day);
});