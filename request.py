import requests
data = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2023-08-27&sortBy=publishedAt&apiKey=a3b6a5f4cc344b9eb13838dda14024d6")
print(type(data.json()))
data = data.json()
print(data["status"])
header = requests.head("https://newsapi.org/v2/everything?q=tesla&from=2023-08-27&sortBy=publishedAt&apiKey=a3b6a5f4cc344b9eb13838dda14024d6")
print(header.headers)
