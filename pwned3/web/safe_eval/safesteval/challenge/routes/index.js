'use strict';
var express = require('express');
var router = express.Router();
var safereval = require('safer-eval');

/* GET home page. */

router.get('/', (req, res) => {
  res.render('./views/index.html', {result:'Enter your calculation down below:'});
});

router.post('/calculator', (req, res) => {
  var postBody = req.body.calculate;
  var regex1 = new RegExp(/[;.f\ *%\r\n]|cd|ls|cat|\\/gm);
  if (regex1.test(postBody)){
    res.render('./views/index.html', {result: 'Bad input!'});
  } else {
    var code = safereval(postBody);
    res.render('./views/index.html', { result: code});
  };
});

module.exports = router;
