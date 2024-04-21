import random
from flask import Flask

app = Flask(__name__)

@app.route('/get_seed')
def get_seed():
    seed = random.randint(-100000000000000000000000, 100000000000000000000000)
    return f'{{ "seed": "{str(seed)}" }}'

@app.route('/')
def seedGen():
    # request_seed() is a function that requests a seed on page's load and while clicking on a "Generate New" button.
    # Line 19: Requests new seed while entering /get_seed URL, then on line 20 on load of the page function()
    # creates an object which parses responseText. Then it creates a new seed on the <span> text line on
    # line 35 after requesting text line with the ID "demo".
    script = '''
function request_seed() {
  const xhttp = new XMLHttpRequest();
  xhttp.onload = function() {
    const obj = JSON.parse(this.responseText);
    document.getElementById("demo").innerHTML = obj.seed;
  }
  xhttp.open("GET", "/get_seed", true);
  xhttp.send();
}
'''
    return '''
<html>
<body onload="request_seed();">

<h1>MC Seed Generator</h1>

<p>Select and press Ctrl+C to Copy (Ctrl+V to Paste).</p>
<p>Seed: <span id="demo">N/A</span></p>
<button class="button" type="button" onclick="request_seed();">Generate New</button>
<p>Good Luck Finding the Best Seed :)</p>

</body>
<script>
  {script}
</script>
</html>
'''

app.run(debug=True, host="0.0.0.0", port=5001)