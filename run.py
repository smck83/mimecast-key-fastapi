import uvicorn


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")


# http://localhost:8000/generate-mc-token/{APPKEY}/?uri={uri}}&access_key={access_key}&secret_key={secret_key}