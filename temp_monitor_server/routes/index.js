var express = require('express');
var router = express.Router();

var lastTempData = {"avgF": 70, "avgC": 21}

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', lastTempData);
});

router.post('/temp_data', function(req, res, next) {
  lastTempData = req.body;
  res.end();
})

module.exports = router;
