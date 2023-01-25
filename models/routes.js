const mongoose = require('mongoose')
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/connection_ssh', {
useNewUrlParser: true,
},
(err) => {
    if (!err) {
        console.log('Connection suceeded');
    } else {
        console.log('Error in connection' + err);
    }
});

require('./routes.model');