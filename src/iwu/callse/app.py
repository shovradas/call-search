from flask import Flask
from iwu.callse import views

app = Flask(__name__)
app.add_url_rule(rule='/', view_func=views.index)
app.add_url_rule(rule='/', view_func=views.index_post, methods=['POST'])
app.add_url_rule(rule='/about', view_func=views.about)


def main():
    # app.run()
    app.run(debug=True)


if __name__ == "__main__":
    main()
