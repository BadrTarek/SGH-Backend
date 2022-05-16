const { JSDOM } = require( "jsdom" );
const { window } = new JSDOM( "" );
const $ = require( "jquery" )( window );




// Django Server
const https = require('https')
const DJANGO_SERVER = 'http:127.0.0.1:8000';
const DJANGO_PORT = 8000;

// var data = {
//     greenhouse_id: 1,
//     password:"mqN9weY",
//     sensors : [
//         {
//             sensor_id:1,
//             value: 10
//         }
//     ]
// };
// var data = '{"greenhouse_id": 1,"password":"mqN9weY","sensors" : [{"sensor_id":1,"value": 10}]}';

$.ajax({
    url: "http://127.0.0.1:8000/hardware/sensors/values/store",
    method:"POST",
    contentType: "application/json",
    dataType: 'json',
    data:data,
    beforeSend: function (xhr) {
        console.log("BeforeSend");
        //xhr.setRequestHeader('Authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0NDAxNzUwLCJpYXQiOjE2NDQzMTUzNTAsImp0aSI6IjA5MjhjYmYyZDI0YTQwNzJiMTUwNzAyM2VkYWJjZTczIiwidXNlcl9pZCI6M30.cGNro-oiDf13AsF8hza3IM1KrjnctNJ1dXzERJanS-U');
    },
    success: function(data){
        console.log("Success");
        console.log(data)
    },
    error: function(xhr, status, err) {
        console.log("Error");
        console.log(xhr);
        console.log(status);
        console.log(err);
    }
});










// HTTP Request To Django Server
function request(path,method,data){
    $.ajax({
        url: DJANGO_SERVER + path,
        method:"POST",
        // dataType:'JSON',
        beforeSend: function (xhr) {
            console.log("BeforeSend");
            //xhr.setRequestHeader('Authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0NDAxNzUwLCJpYXQiOjE2NDQzMTUzNTAsImp0aSI6IjA5MjhjYmYyZDI0YTQwNzJiMTUwNzAyM2VkYWJjZTczIiwidXNlcl9pZCI6M30.cGNro-oiDf13AsF8hza3IM1KrjnctNJ1dXzERJanS-U');
        },

        success: function(data){
            console.log(data)
        },
        error: function(xhr, status, err) {
            console.log(xhr);
            console.log(status);
            console.log(err);
        }
    });
    
    // $.post( ("http://127.0.0.1:8000" + path ), data ,function(data){
    //     alert("Data: " + data);
    // });

    // const options = {
    //     hostname: DJANGO_SERVER,
    //     port: DJANGO_PORT,
    //     path: "/hardware/actuator/action",
    //     method: "POST"
    // }

    // const req = https.request(options, res => {
    //     console.log(`statusCode: ${res.statusCode}`)

    //     res.on('data', d => {
    //         print(d)
    //         process.stdout.write(d)
    //     })

    // })

    // req.on('error', error => {
    //     console.error(error)
    // })

    // req.end()

}

// Socket.io Server
const { Server } = require("socket.io");

// Define the port of NodeJS Server
const PORT = 4000;

// Socket.io Server Settings
serverOptions = {
    cors: {
        origin: '*',
        credentials: false,
    },
}

// Define Socket.io Instance
const io = new Server(serverOptions);

// Define The Clients Namespaces
const HARDWARE_NAMESPACE = io.of("/hardware");
const WEB_NAMESPACE = io.of("/web");
const MOBILE_NAMESPACE = io.of("/mobile");

// Hardware
HARDWARE_NAMESPACE.on("connection", (socket) => {

    console.log(`Hardware Client Connected with ID = ${socket.id}`);

    socket.on("sensors_values", data => {
        console.log(data);
        request('/hardware/sensors/values/store',"POST");
        WEB_NAMESPACE.emit("sensors_values", data);
        MOBILE_NAMESPACE.emit("sensors_values", data)
    });


});

// Web
WEB_NAMESPACE.on("connection", (socket) => {

    console.log(`Web Client Connected with ID = ${socket.id}`);

    socket.on("take_action", data => {
        console.log(data);
        HARDWARE_NAMESPACE.emit("take_action", data)
        // MOBILE_NAMESPACE.emit(data)
    });


});




// io.listen(3000);
io.listen(PORT, () => console.log('listening on port 4000'))
