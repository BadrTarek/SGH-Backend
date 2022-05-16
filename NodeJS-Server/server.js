// For Express & Socket.io
const express = require("express");
const { createServer } = require("http");
const { Server } = require("socket.io");
const PORT = 3000;
const app = express();
const httpServer = createServer(app);
const io = new Server(httpServer, {
    cors: {
        origin: '*',
        credentials: false,
    },
});
const HARDWARE_NAMESPACE = io.of("/");
const WEB_NAMESPACE = io.of("/web");
const MOBILE_NAMESPACE = io.of("/mobile");

// For Jquery
const { JSDOM } = require( "jsdom" );
const { window } = new JSDOM( "" );
const $ = require( "jquery" )( window );


// For Django
const https = require('https')
const DJANGO_SERVER = 'http://127.0.0.1';
const DJANGO_PORT = 8000;
const DJANGO_URL = DJANGO_SERVER + ":" + DJANGO_PORT;


// Hardware Clients
HARDWARE_NAMESPACE.on("connection", (socket) => {

    console.log(`Hardware Client Connected with ID = ${socket.id}`);
    response = '{"status_code":200,"message":"Hardware Connected Successfully"}';

    WEB_NAMESPACE.emit("hardware_connection",JSON.parse(response));
    MOBILE_NAMESPACE.emit("hardware_connection",JSON.parse(response));


    socket.on("sensors_values", data => {
        console.log(data);

        $.ajax({
            url: DJANGO_URL + '/hardware/sensors/values/store',
            method:"POST",
            contentType: "application/json",
            dataType: 'json',
            data:JSON.stringify(data),
            beforeSend: function (xhr) {
                //xhr.setRequestHeader('Authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0NDAxNzUwLCJpYXQiOjE2NDQzMTUzNTAsImp0aSI6IjA5MjhjYmYyZDI0YTQwNzJiMTUwNzAyM2VkYWJjZTczIiwidXNlcl9pZCI6M30.cGNro-oiDf13AsF8hza3IM1KrjnctNJ1dXzERJanS-U');
            },
            success: function(data){
                console.log("Successfully");
                WEB_NAMESPACE.emit("sensors_values", data);
                MOBILE_NAMESPACE.emit("sensors_values", data);
            },
            error: function(xhr, status, err) {
                console.log("Error");
                console.log(xhr);
                console.log(status);
                console.log(err);
            }
        });

        $.ajax({
            url: DJANGO_URL + '/hardware/automated/action',
            method:"POST",
            contentType: "application/json",
            dataType: 'json',
            data:JSON.stringify(data),
            beforeSend: function (xhr) {
                //xhr.setRequestHeader('Authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0NDAxNzUwLCJpYXQiOjE2NDQzMTUzNTAsImp0aSI6IjA5MjhjYmYyZDI0YTQwNzJiMTUwNzAyM2VkYWJjZTczIiwidXNlcl9pZCI6M30.cGNro-oiDf13AsF8hza3IM1KrjnctNJ1dXzERJanS-U');
            },
            success: function(data){
                console.log("Successfully");
                HARDWARE_NAMESPACE.emit("take_automated_action", data);
            },
            error: function(xhr, status, err) {
                console.log("Error");
                console.log(xhr);
                console.log(status);
                console.log(err);
            }
        });


    });
    
    socket.on("disconnect", () => {
        console.log(`Hardware Client DisConnected with ID = ${socket.id}`);

        response = '{"status_code":501,"message":"Hardware Disconnected"}';

        WEB_NAMESPACE.emit("hardware_connection",JSON.parse(response))
        MOBILE_NAMESPACE.emit("hardware_connection",JSON.parse(response))
    });

});



// Web Clients
WEB_NAMESPACE.on("connection", (socket) => {

    console.log(`Web Client Connected with ID = ${socket.id}`);
    
    socket.on("take_action", data => {
        console.log(data);
        
        
        $.ajax({
            url: DJANGO_URL + '/hardware/actuator/action',
            method:"POST",
            contentType: "application/json",
            dataType: 'json',
            data:JSON.stringify(data),
            beforeSend: function (xhr) {
                //xhr.setRequestHeader('Authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0NDAxNzUwLCJpYXQiOjE2NDQzMTUzNTAsImp0aSI6IjA5MjhjYmYyZDI0YTQwNzJiMTUwNzAyM2VkYWJjZTczIiwidXNlcl9pZCI6M30.cGNro-oiDf13AsF8hza3IM1KrjnctNJ1dXzERJanS-U');
            },
            success: function(data){
                console.log("Successfully");

                HARDWARE_NAMESPACE.emit("take_action",data);

                WEB_NAMESPACE.emit("action_taked", data);
                MOBILE_NAMESPACE.emit("action_taked", data);
            },
            error: function(xhr, status, err) {
                console.log("Error");
                console.log(xhr);
                console.log(status);
                console.log(err);
            }
        });

    });
    
    socket.on("disconnect", () => {
        console.log(`Web Client DisConnected with ID = ${socket.id}`);
    });


});


MOBILE_NAMESPACE.on("connection", (socket) => {

    console.log(`Mobile Client Connected with ID = ${socket.id}`);
    
    socket.on("take_action", data => {
        console.log(data);
        
        
        $.ajax({
            url: DJANGO_URL + '/hardware/actuator/action',
            method:"POST",
            contentType: "application/json",
            dataType: 'json',
            data:JSON.stringify(data),
            beforeSend: function (xhr) {
                //xhr.setRequestHeader('Authorization', 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQ0NDAxNzUwLCJpYXQiOjE2NDQzMTUzNTAsImp0aSI6IjA5MjhjYmYyZDI0YTQwNzJiMTUwNzAyM2VkYWJjZTczIiwidXNlcl9pZCI6M30.cGNro-oiDf13AsF8hza3IM1KrjnctNJ1dXzERJanS-U');
            },
            success: function(data){
                console.log("Successfully");

                HARDWARE_NAMESPACE.emit("take_action",data);

                WEB_NAMESPACE.emit("action_taked", data);
                MOBILE_NAMESPACE.emit("action_taked", data);
            },
            error: function(xhr, status, err) {
                console.log("Error");
                console.log(xhr);
                console.log(status);
                console.log(err);
            }
        });

    });
    
    socket.on("disconnect", () => {
        console.log(`Mobile Client DisConnected with ID = ${socket.id}`);
    });

});

httpServer.listen(PORT,()=>{
    console.log("****************** Listening on port " + PORT + " ******************");
});