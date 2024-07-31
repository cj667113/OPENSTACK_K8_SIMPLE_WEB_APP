from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def fetch_data():
	url = 'http://169.254.169.254/1.0/meta-data/hostname'
	response=requests.get(url)
	if response.status_code==200:
		return response.text
	else:
		return f'Failed to fetch data: {response.status_code}'
if __name__ == '__main__':
	app.run(debug=True)
