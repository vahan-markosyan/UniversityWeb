from flask import Flask, render_template 
 
app = Flask(__name__)  # Use name here 
 
@app.route('/') 
def home(): 
    return render_template('index.html')  # Render the HTML file 
 
if __name__ == '__main__':  # Use name to check if the script is run directly 
    app.run(debug=True)