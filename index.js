require('./models/routes')
const express = require('express')
const path = require('path')
const handlebars = require('handlebars')
const exphbs = require('express-handlebars')
const {allowInsecurePrototypeAccess} = require('@handlebars/allow-prototype-access')
const bodyparser = require('body-parser')
const { engine } = require('express-handlebars');
const routes_controller = require('./controllers/routes_controller')

var app = express();

app.use(bodyparser.urlencoded({extended: false}))
app.use(bodyparser.json())

app.get('/', (req, res) => {
    res.send(`
    <center><h2>Welcome to REMOTE CONNECTION</h2></center>
    <p></p>
    <center><h3>Click hereto get access to the <b> <a href="/router/list">Home</a></b></h3></center>
   `);
    
});

app.set('views', path.join(__dirname, "/views/"));

app.engine('hbs', exphbs.engine({
        handlebars: allowInsecurePrototypeAccess(handlebars),
        extname: 'hbs',
        defaultLayout: "mainLayout",
        layoutsDir: __dirname + "/views/layouts/",
    })
);

const port = process.env.PORT || 3000
app.listen(port, () => {
console.log(`Server started at port ${port}`)
});

app.set('view engine', 'hbs');

app.listen(3000, () => {
    console.log("server started at port 3000")
});

app.use('/router', routes_controller);

