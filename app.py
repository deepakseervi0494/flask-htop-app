from flask import Flask
import os
import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the current time in IST (Indian Standard Time)
    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

    # Get system username
    username = os.getenv("USER") or os.getenv("USERNAME") or "Unknown"

    # Run the 'top' command and get the first 10 lines
    top_output = "\n".join(os.popen("top -b -n 1 | head -10").read().splitlines())

    # Return the response as an HTML page
    return f"""
    <html>
        <head>
            <title>/htop</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 20px;
                }}
                h1, h2 {{
                    color: #333;
                }}
                pre {{
                    background: #f4f4f4;
                    padding: 10px;
                    border-radius: 5px;
                    overflow-x: auto;
                }}
            </style>
        </head>
        <body>
            <h1>Name: Deepak Seervi</h1>
            <h2>Username: {username}</h2>
            <h2>Server Time (IST): {server_time}</h2>
            <h3>Top Output:</h3>
            <pre>{top_output}</pre>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
