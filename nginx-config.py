from settings.settings import Settings
from render.render import Render

if __name__ == "__main__":
    s = Settings()
    r = Render(s)
    r.render()
