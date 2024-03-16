import random
from flask import Flask

app = Flask(__name__)

@app.route('/')
def seedGen():
    seed = random.randint(-100000000000000000000000, 100000000000000000000000)
    return f'''
<html>
<body>

<h1>MC Seed Generator</h1>

<p>Select and press Ctrl+C to Copy (Ctrl+V to Paste).</p>
<p>Seed: {str(seed)}</p>

<p>Good Luck Finding the Best Seed :)</p>

</body>
</html>
'''

app.run(debug=True)