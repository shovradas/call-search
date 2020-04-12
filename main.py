from flask import Flask
import views

app = Flask(__name__)
app.add_url_rule(rule='/', view_func=views.index)
app.add_url_rule(rule='/about', view_func=views.about)

if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
