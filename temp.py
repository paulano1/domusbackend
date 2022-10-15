import requests
def getImages(text):
    key = "563492ad6f91700001000001636eabc8f29d4a39922b8f4a197f2b7d"
    header = {
        "Authorization": key
    }
    response = requests.get("https://api.pexels.com/v1/search?query="+text+"&per_page=1", headers=header)
    print(response.json()["photos"][0]["src"]["original"])

getImages("setting+sun")