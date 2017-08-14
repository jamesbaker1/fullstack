var express = require('express');
var bodyParser = require('body-parser'); // For json data
const crypto = require('crypto'); // Encryption
var _ = require('lodash'); // Quick lookup within object

var app = express();
app.use(bodyParser.json());

const hashList = {} // Local storage, could eventually migrate to some sort of database (mongo?)

app.post('/messages', (req, res) => {
  const { message } = req.body;
  let hash = _.findKey(hashList, message);
  // Couldn't find message within storage
  if (!hash) {
    hash = crypto.createHash('sha256').update(message).digest("hex");
    hashList[hash] = message;
  }
  res.status(200).send({ digest: hash });
})

app.get('/messages/:hash', (req, res) => {
  if (req.params.hash in hashList) {
    res.send({ message: hashList[req.params.hash] })
  } else {
    res.sendStatus(404);
  }
})

app.listen(3030, () => {
  console.log('Server listening on port 3030');
});


// Limiting factors as users grow:
// Local storage vs. Database
// Having to look up by keys in hashList is O(n) time,
// could potentially keep two objects, one with the hash as the key
// and one with the message as the key to reduce to constant time
