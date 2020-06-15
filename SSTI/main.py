from flask import Flask, request, render_template_string
from jinja2 import Template

app = Flask(__name__)
app.config.from_pyfile('config.py')

@app.route("/",  methods=['GET'])
def get_username():
    return render_template_string(
        """
        <form action="/hello">
            <label for="username">Enter username:</label><br>
            <input type="text" size="50" name="username" ><br>
            <input type="submit" value="Submit">
        </form> 
        """
    )

@app.route("/hello",  methods=['GET', 'POST'])
def say_hello():
    username = request.args.get('username')
    template = Template(
        """
        <h2> Hello <i style='color: royalblue;'> \
            {{ username }} </i>! Nice to meet you </h2>
        """
    )
    source = template.render(username=username)
    a = render_template_string(source)
    return a

if __name__ == '__main__':
    app.run(debug=True)
