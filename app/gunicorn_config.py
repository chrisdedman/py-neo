"""Gunicorn configuration file."""
import multiprocessing

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

workers = multiprocessing.cpu_count() * 2 + 1
bind = "0.0.0.0:8000" 
timeout = 30
loglevel = "info" 
errorlog = "-"  # "-" means stderr
accesslog = "-"  # "-" means stderr
chdir = "."  # Set to the current directory