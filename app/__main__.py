import uvicorn
from app import application


def main():
    # FIXME: remove host and post
    uvicorn.run(application, host="0.0.0.0", port=8000)  # nosec


if __name__ == '__main__':
    main()
