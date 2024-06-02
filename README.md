# Gomoku Game

This is a simple web-based Gomoku game built with Python, Flask, and Socket.IO. The game allows users to set the board size and play Gomoku interactively.

## Features

- Set custom board size (default is 15x15)
- Interactive game board
- Real-time updates using Socket.IO
- Simple game logic implemented in Python

## Requirements

- Python 3.x
- Flask
- Flask-SocketIO

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/gomoku-game.git
   cd gomoku-game
   
2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. Install the required packages:
  
   ```bash
   pip install Flask Flask-SocketIO

## Running the Application

1. Start the Flask application:

   ```bash
   python app.py

2. Open your web browser and navigate to `http://127.0.0.1:5001/`.

## Project Structure

- `app.py`: The main Flask application file that sets up routes and handles Socket.IO events.
- `gomoku.py`: Contains the game logic for Gomoku.
- `templates/index.html`: The main HTML file for the front-end, includes JavaScript and CSS for the game.
- `static/`: Directory for static files like CSS and JavaScript (if needed).

## Usage

- **Set Board Size**: Enter a board size between 5 and 20 and click "Set Board Size".
- **Make a Move**: Click on the cells to place your move. The game will automatically switch turns between 'X' and 'O'.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
