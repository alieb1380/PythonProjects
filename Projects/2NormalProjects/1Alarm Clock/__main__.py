try:
    from app import app
except ImportError:
    from .app import App
    
    
if __name__ == "__main__":
    app = App(600, 185)
    app.start()