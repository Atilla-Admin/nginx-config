from settings.settings import Settings
from actions.render import Render

if __name__ == "__main__":
    s = Settings()
    r = Render(s)
    r.render()
