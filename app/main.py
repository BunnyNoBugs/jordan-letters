from flask import Flask
from flask import render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><p>Hello, world!</p></body></html>'

@app.route('/name')
@app.route('/name/<name>')
def name(name):
    with open('../letter.xml', encoding='utf-8') as f:
        letter_text = f.read()
    soup = BeautifulSoup(letter_text, 'html.parser')
    ps_with_name = []
    for p in soup.find_all('p'):
        if p.find('rs', {'ref': '#'+name}) or p.find('persName', {'ref': '#'+name}):
            new_p_spl = []
            new_p = str(p)
            for tag in p.find_all('persname', {'ref': '#'+name}):
                new_p = new_p.replace(str(tag), f'^{tag.get_text()}^')
            for tag in p.find_all('rs', {'ref': '#'+name}):
                new_p = new_p.replace(str(tag), f'^{tag.get_text()}^')
            for i, part in enumerate(BeautifulSoup(new_p, 'html.parser').get_text().split('^')):
                new_p_spl.append((i, part))
            ps_with_name.append(new_p_spl)
    return render_template('name.html', ps_with_name=ps_with_name)


if __name__ == '__main__':
    app.run(debug=False)