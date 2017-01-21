var express = require('express');
var moment = require('moment');
var router = express.Router();

var lastTempData = {"avgF": 70, "avgC": 21, "timestamp": moment().format("MM-DD-YY h:mm:ss a")}

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', lastTempData);
});

router.post('/temp_data', function(req, res, next) {
  lastTempData = req.body;
  lastTempData.timestamp = moment().format("MM-DD-YY h:mm:ss a");
  res.end();
})

module.exports = router;
