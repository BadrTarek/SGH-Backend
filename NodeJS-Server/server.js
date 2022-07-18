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

    socket.on("authorization",data =>{
        $.ajax({
            url: DJANGO_URL + '/product/login',
            method:"POST",
            contentType: "application/json",
            dataType: 'json',
            data:JSON.stringify(data),
            success: function(data){
                if(data.status_code == 200){
                    console.log("Hardware Authorized Successfully");
                    HARDWARE_NAMESPACE.emit("token",data);
                    socket.join(data.product.id);
                }else{
                    console.log("Hardware Authorization Faild and Disconnected");
                    socket.disconnect();
                }
            },
            error: function(xhr, status, err) {
                console.log("Error");
                console.log(xhr);
                console.log(status);
                console.log(err);
            }
        });

    });

    socket.on("sensors_values", data => {
        console.log(data);

        if(data.token){
            $.ajax({
                url: DJANGO_URL + '/hardware/sensors/values/store',
                method:"POST",
                contentType: "application/json",
                dataType: 'json',
                data:JSON.stringify(data),
                beforeSend: function (xhr) {
                    xhr.setRequestHeader('Authorization', data.token);
                },
                success: function(data){
                    console.log("Stored Sensor Successfully");
                    // orderNamespace.to("room1").emit("hello")
                    WEB_NAMESPACE.emit("sensors_values", data);
                    MOBILE_NAMESPACE.emit("sensors_values", data);
                },
                error: function(xhr, status, err) {
                    console.log(xhr);
                    console.log(err);
                    console.log(status);
                    console.log("!!!!!!!!!!!! Error in Store Sensor Values Request !!!!!!!!!!!!");
                }
            });

            $.ajax({
                url: DJANGO_URL + '/hardware/automated/action',
                method:"POST",
                contentType: "application/json",
                dataType: 'json',
                data:JSON.stringify(data),
                beforeSend: function (xhr) {
                    xhr.setRequestHeader('Authorization', data.token);
                },
                success: function(data){

                    if(data.status_code==200)
                    {
                        console.log("Autometed Action Requested Successfully");
                        HARDWARE_NAMESPACE.emit("take_automated_action", data);
                    }
                },
                error: function(xhr, status, err) {
                    console.log("!!!!!!!!!!!! Error in Automated Action Request !!!!!!!!!!!!");
                }
            });
        }else{
            console.log("!!!!!!!!!!!! The Hardware Not Authorized So It Has Been Removed !!!!!!!!!!!!");
            socket.disconnect();
        }

    });

    socket.on("fire_detected", data => {
        console.log(data);

        if(data.token){
            $.ajax({
                url: DJANGO_URL + '/product/fire',
                method:"GET",
                contentType: "application/json",
                dataType: 'json',
                data:JSON.stringify(data),
                beforeSend: function (xhr) {
                    xhr.setRequestHeader('Authorization', data.token);
                },
                success: function(data){
                    console.log("User Notified With The Fire Successfully");
                },
                error: function(xhr, status, err) {
                    console.log("!!!!!!!!!!!! Fire Alarm Request !!!!!!!!!!!!");
                }
            });
        }else{
            console.log("!!!!!!!!!!!! The Hardware Not Authorized So It Has Been Removed !!!!!!!!!!!!");
            socket.disconnect();
        }

    });

    socket.on("actuator_status",data=>{
        if(data.token){
            delete data.token;
            WEB_NAMESPACE.emit("actuator_status", data);
            MOBILE_NAMESPACE.emit("actuator_status", data);
        }else{
            socket.disconnect();
        }
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

        if(data.token){
            $.ajax({
                url: DJANGO_URL + '/hardware/actuator/action',
                method:"POST",
                contentType: "application/json",
                dataType: 'json',
                data:JSON.stringify(data),
                beforeSend: function (xhr) {
                    xhr.setRequestHeader('AUTHORIZATION', 'Bearer ' + data.token);
                },
                success: function(data){
                    console.log("Take Action Requested Successfully");
                    HARDWARE_NAMESPACE.emit("take_action",data);
                },
                error: function(xhr, status, err) {
                    console.log("Error");
                    console.log(xhr);
                    console.log(status);
                    console.log(err);
                }
            });

        }else{
            console.log("!!!!!!!!!!!! The Web Not Authorized So It Has Been Removed !!!!!!!!!!!!");
            socket.disconnect();
        }
    });

    socket.on("disconnect", () => {
        console.log(`Web Client DisConnected with ID = ${socket.id}`);
    });


});


MOBILE_NAMESPACE.on("connection", (socket) => {

    console.log(`Mobile Client Connected with ID = ${socket.id}`);

    socket.on("take_action", data => {
        console.log(data);

        if(data.token)
        {
            $.ajax({
              url: DJANGO_URL + '/hardware/actuator/action',
              method:"POST",
              contentType: "application/json",
              dataType: 'json',
              data:JSON.stringify(data),
              beforeSend: function (xhr) {
                  xhr.setRequestHeader('AUTHORIZATION', 'Bearer ' + data.token);
              },
              success: function(data){
                console.log("Take Action Requested Successfully");

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
        }else{
            console.log("!!!!!!!!!!!! The Mobile Not Authorized So It Has Been Removed !!!!!!!!!!!!");
            socket.disconnect();
        }

    });

    socket.on("disconnect", () => {
        console.log(`Mobile Client DisConnected with ID = ${socket.id}`);
    });

});

httpServer.listen(PORT,()=>{
    console.log("****************** Listening on port " + PORT + " ******************");
});
