import express from 'express';
import { SERVER_IP, SERVER_PORT } from './consts';

import http from 'http';
import WebSocket from 'ws';


console.log( "TEST" );



// website
const app = express();
app.use( express.static( 'public' ) );
app.listen( SERVER_PORT, SERVER_IP, () => {
  console.log( `Web server listening on ${ SERVER_IP }:${ SERVER_PORT }` );
} );

app.get( '/', ( req, res ) => {
  res.sendFile( 'index.html' );
} );


// data from dataGatherer
const httpServer = http.createServer( app );
const wsServer = new WebSocket.Server( { server: httpServer } );
wsServer.on( 'connection', ( ws ) => {
  ws.on( 'message', ( message ) => {
    console.log( `Received message => ${ message }` );
    ws.send( `You sent => ${ message }` );
  } );
} );