const mongoose = require('mongoose')

var routerSchema = new mongoose.Schema({
    ip: { type: String, required: ' This field is required', },
    username: { type: String, required: ' This field is required', },
    
});

mongoose.model("Routes", routerSchema);
