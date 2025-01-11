"use strict";
var board = new Image();
board.src = 'static/unknown_board.jpg';

//const my_streamer_game_uuid = my_streamer_game_uuid;

//const { my_streamer_game_uuid } = require('./type_game_uuid.js');


const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const game_uuid_for_watchers = urlParams.get('game_uuid_for_watchers')
console.log(game_uuid_for_watchers);


const board_canvas = document.getElementById("go-board");

const board_context = board_canvas.getContext("2d");


/*

do {

    update_watched_board();
}
while (true);
*/


setInterval(function() {
    // Do something every 3 seconds
    update_watched_board();
}, 3000);



async function update_watched_board(){
    var response = await fetch('/request_updates_in_game_being_watched', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({streamer_game_uuid:game_uuid_for_watchers}),
    })

    if(response.status == 502){
        console.log('Update failed');
        return;
    } else {
        var data = await response.json();
        board.src = 'data:image/jpeg;base64,' + data.image;
        console.log(data.image);
        board_context.drawImage(board, 0, 0);
        //game_uuid = data.game_uuid

        //MESSAGE = data.message;
    }
}
