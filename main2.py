import threading
import copy
from ultralytics import YOLO
from GoGame import *
from GoBoard import *
from GoVisual import *
from flask import Flask, render_template, Response, request, send_file
import cv2
import base64

cam_index = 0

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'  



model = YOLO('model.pt')

usual_message = "La caméra est bien fixée et tout est Ok"
message = "Rien n'a encore été lancé "
# disabled_button = 'stop-button'


ProcessFrame = None
Process = True
initialized = False
sgf_text = None
empty_board = cv2.imread("static/empty_board.jpg")
game_plot = empty_board
process_thread = None
go_game = None
transparent_mode = False


def New_game(transparent_mode=False):
    
    global go_game, initialized, game_plot
    game = sente.Game()
    go_visual = GoVisual(game)
    go_board = GoBoard(model)
    go_game = GoGame(game, go_board, go_visual, transparent_mode)
    game_plot = empty_board
    initialized = False

def processing_thread():
    """
        Process the detection algorithm
        
        Update:
            game_plot, sgf_text
        Send error to message if there is one
        """
    
    global ProcessFrame, game_plot, message, initialized, sgf_text

    if not ProcessFrame is None:
        try:
            if not initialized:
                game_plot = go_game.initialize_game(ProcessFrame)
                initialized = True
                message = usual_message
            else:    
                game_plot, sgf_text = go_game.main_loop(ProcessFrame)
                message = usual_message
        except Exception as e:
            message = "Erreur : "+str(e)
                
def generate_plot():
    """
        Generate a plot representing the game
        
        Returns:
            Image
        """
    global game_plot
    
    processing_thread()
    if transparent_mode:
        to_plot = game_plot
    else:
        to_plot = go_game.go_visual.current_position()
    
    _, img_encoded = cv2.imencode('.jpg', to_plot)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')

    return img_base64

@app.route('/')
def index():
    """Route to display HTML page"""
    return render_template('Home.html')

@app.route('/home')
def home():
    """Route to display HTML page"""
    return render_template('Home.html')

@app.route('/update')
def afficher_message():
    """
        Route to update the image and the message to display 
        
        Returns:
            message
            image
    """

    return {'message': message, 'image' : generate_plot()}


@app.route('/controls', methods=["POST"])
def controls():
    """
        Change the current move
    """
    print(request.data)
    # go_game.go_visual.next()
    return Response(status=204)


@app.route('/upload', methods=['POST'])
def process():
    """
        Route which enables us to load the sgf text
        """
    global transparent_mode
    
    transparent_mode = False
    file = request.files['file']
    file_path = file.filename
    try:
        print("fileee", file_path)
        New_game()
        go_game.go_visual.load_game_from_sgf(file_path)
        print("######################## loaaaaded")
        message = "Le fichier a été correctement chargé"
    except Exception as e:
        print("######################## Not loaaaaded")
        message = "L'erreur est " + str(e)

    return Response(status=204)
    # return Response()
    # return render_template('sgf.html')

@app.route('/credit')
def credit():
    """
        Route to get to the credit page
        """
    return render_template("credits.html")


    
@app.route('/historique')
def historique():
    """
        Route to get to the summary page
    """
    return render_template("Historique.html")


@app.route('/game')
def game():
    """
    Route to get to the streaming page in game mode
    """
    global transparent_mode
    
    transparent_mode = False

    return render_template("game.html")

@app.route('/transparent')
def transparent():
    """
        Route to get to the streaming page in transparent mode
        """
    go_game.set_transparent_mode(True)
    global transparent_mode
    
    transparent_mode = False
    return render_template("transparent.html")

@app.route('/sgf')
def sgf():
    """
        Route to get to the streaming page in transparent mode
        """
    global transparent_mode
    
    transparent_mode = False
    return render_template("sgf.html")



if __name__ == '__main__':
    # New_game()
    # process_thread = threading.Thread(target=processing_thread, args=())
    # process_thread.start()
    app.run(debug=True)
    
# %%