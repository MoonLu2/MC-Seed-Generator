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
<form>
<p>Seed: {str(seed)}</p>
</form>
<button class="button" type="button" onclick="">Generate New</button>

<p>Good Luck Finding the Best Seed :)</p>

</body>
</html>
'''

app.run(debug=True, host="0.0.0.0", port=5001)