const express = require('express')
const app = express()

const { JSDOM } = require( "jsdom" );
const { window } = new JSDOM( "" );
const $ = require( "jquery" )( window );




// Django Server
const https = require('https')
const DJANGO_SERVER = 'http://127.0.0.1';
const DJANGO_PORT = 8000;
const DJANGO_URL = DJANGO_SERVER + ":" + DJANGO_PORT;


// HTTP Request To Django Server
function request(path,method,send_data){
    let return_data = false ;
    $.ajax({
        url: DJANGO_URL + path,
        method:method,
        contentType: "application/json",
        dataType: 'json',
        data:JSON.stringify(send_data),
        beforeSend: function (xhr) {
            //xhr.setRequestHeader('Authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0NDAxNzUwLCJpYXQiOjE2NDQzMTUzNTAsImp0aSI6IjA5MjhjYmYyZDI0YTQwNzJiMTUwNzAyM2VkYWJjZTczIiwidXNlcl9pZCI6M30.cGNro-oiDf13AsF8hza3IM1KrjnctNJ1dXzERJanS-U');
        },
        success: function(data){
            console.log("Success");
            // console.log(data);
            return_data =  data;
            // console.log("data" + data);
            // console.log("return_data)" + return_data );

            console.log("Bedaaaaaaaan");
        },
        error: function(xhr, status, err) {
            console.log("Error");
            console.log(xhr);
            console.log(status);
            console.log(err);
        }
    });
    console.log(return_data);
    return return_data;
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
        // let recieved_data = request('/hardware/sensors/values/store',"POST",data)
        WEB_NAMESPACE.emit("sensors_values",request('/hardware/sensors/values/store',"POST",data) );
        // if(recieved_data)
        //MOBILE_NAMESPACE.emit("sensors_values", request('/hardware/actuator/action',"POST",data));
    });


});

// Web
WEB_NAMESPACE.on("connection", (socket) => {

    console.log(`Web Client Connected with ID = ${socket.id}`);

    socket.on("take_action", data => {
        console.log(data);
        var recieved_data = request('/hardware/actuator/action',"POST",data);
        HARDWARE_NAMESPACE.emit("take_action",recieved_data )
        // if(recieved_data)
        // MOBILE_NAMESPACE.emit(data)
    });


});




// io.listen(3000);
io.listen(PORT, () => console.log('listening on port 4000'))
