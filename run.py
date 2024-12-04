import os
os.environ["OMP_NUM_THREADS"] = '1'

from main import app


if __name__ == '__main__':
    app.run(debug=True, threaded=True, host='0.0.0.0', port = 5000)
