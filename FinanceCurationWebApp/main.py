from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("Hello, World")
    return render_template('index.html', name='pyCharm')

if __name__ == '__main__':
    app.run()

# local host db
#  CREATE TABLE `fincura`.`users` (`name` VARCHAR(80) NOT NULL , `email` VARCHAR(254) NOT NULL , `password` VARCHAR(60) NOT NULL ) ENGINE = InnoDB;