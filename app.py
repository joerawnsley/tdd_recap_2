from flask import Flask, render_template
import db
app = Flask(__name__)



@app.route('/')
def index():
  coins = db.get_coins()
  return render_template("index.html", coins=coins)

@app.route('/automate')
def automate():
  return render_template("automate.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
