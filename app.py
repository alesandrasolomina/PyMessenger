from flask import Flask
from flask import request

app = Flask(__name__)
ListOfMessages = []

@app.route('/')
def hello_world():
    return 'Messenger Flask server is running! ' \
           '<br> <a href="/status">Check status</a>'

@app.route('/status')
def status():
    return {
        'messages_count': len(ListOfMessages)
    }

@app.route("/api/PyMessenger", methods=['POST'])
def SendMessage():
    msg = request.json
    print(msg)
    ListOfMessages.append(msg)

    msgtext = f"{msg['UserName']} <{msg['TimeStamp']}>: {msg['MessageText']}"
    print(f"Всего сообщений: {len(ListOfMessages)} Посланное сообщение: {msgtext}")
    return f"Сообщение отослано успешно. Всего сообщений: {len(ListOfMessages)} ", 200

@app.route("/api/PyMessenger/<int:id>")
def GetMessage(id):
    print(id)
    if id >= 0 and id < len(ListOfMessages):
        print(ListOfMessages[id])
        return ListOfMessages[id], 200
    else:
        return "Not found", 400

if __name__ == '__main__':
    app.run()
