const mongoose = require('mongoose')

var routerSchema = new mongoose.Schema({
    username: { type: String, required: ' This field is required', },
    ip: { type: String, required: ' This field is required', },
    
});

mongoose.model("Routes", routerSchema);
