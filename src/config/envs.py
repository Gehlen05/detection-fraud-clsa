import os
import socket


def get_chat() -> str:
    return os.environ.get('CHAT_SPACE', 'AAAAk8j4OrU')


def get_chat_key() -> str:
    return os.environ.get('CHAT_KEY', 'AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI')


def get_chat_token() -> str:
    return os.environ.get('CHAT_TOKEN', 'l_oAc0HwcnygbJGLcO15_A8PIUob2jCSS9gzoGC6Lz8')


def get_chat_imagem() -> str:
    return os.environ.get('CHAT_IMAGE', 'https://epipoca.com.br/wp-content/uploads/2021/07/Marvel-What-If-Watcher-Uatu-Concept-Art.jpg')


def get_drive_folder() -> str:
    return os.environ.get('DRIVE_FOLDER', '1zc1FAcKeY-EBlmClvb42KvPHU0_Kou-Z')


def get_log_level() -> str:
    return os.environ.get('LOG_LEVEL', 'info')


def get_server_port() -> int:
    return os.environ.get('SERVER_PORT', 5000)


def get_server_host() -> int:
    hostname = socket.gethostname()
    server_IPAddr = socket.gethostbyname(hostname)
    return os.environ.get('SERVER_HOST', server_IPAddr)

def get_influxdb() -> str:
    return os.environ.get('INFLUXDB_TOKEN', 'SEM_TOKEN')