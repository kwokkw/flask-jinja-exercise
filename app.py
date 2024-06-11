from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config["SECRET_KEY"] = "KEYS"

debug = DebugToolbarExtension(app)


@app.route("/")
def home_page():
    story_prompts = story.prompts
    return render_template("base.html", story_prompts=story_prompts)


@app.route("/story")
def story_page():
    ans = {}
    for prompt in story.prompts:
        ans[prompt] = request.args.get(f"{prompt}")
    text = story.generate(ans)
    return render_template("story.html", text=text)
