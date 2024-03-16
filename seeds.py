# importing Flusk() from flusk library and random library
import random
from flask import Flask

# creating the site
app = Flask(__name__)

# creating a page in the path. You can write after / the name, if you don't want to do that on the main page
@app.route('/')

# Python code function that returns HTML code of the page.
def seedGen():
    seed = random.randint(-100000000000000000000000, 100000000000000000000000)
    return f'''
<html>
<body>

<h1>You're Title</h1> <!Please Make a Different Title>

<p>Select and press Ctrl+C to Copy (Ctrl+V to Paste).</p>
<p>Seed: {str(seed)}</p>

<p>Good Luck Finding the Best Seed :)</p>

<a href=https://github.com/MoonLu2/MC-Seed-Generator/edit/master/seeds.py> Original by: MoonLu2 </a> 
<!Don't remove the link if you want to publish you're site.>
</body>
</html>
'''
# Run the site
app.run(debug=True) # or False
