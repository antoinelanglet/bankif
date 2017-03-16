'use strict';

// Assign hapi.js module to a Hapi variable
const Hapi = require('hapi');
const Good = require('good');

// Creates a server instance
const server = new Hapi.Server();
server.connection({ port: 3000, host: 'localhost' });

// Dynamically adds all the routes to the server instance. The routes are stored in the src/routes folder
for (var route in routes) {
    server.route(routes[route]);
}

server.register({
    register: Good,
    options: {
        reporters: {
            console: [{
                module: 'good-squeeze',
                name: 'Squeeze',
                args: [{
                    response: '*',
                    log: '*'
                }]
            }, {
                module: 'good-console'
            }, 'stdout']
        }
    }
}, (err) => {

    if (err) {
        throw err; // something bad happened loading the plugin
    }

// Starts the hapi.js server
    server.start((err) => {

        if (err) {
            throw err;
        }
        server.log('info', 'Server running at: ' + server.info.uri);
    });
});
