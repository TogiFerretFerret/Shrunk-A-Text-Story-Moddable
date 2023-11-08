class FileReader:
  def __init__(self):
    pass
  def read(self, filename):
    try:
      with open(f"{filename}", "r") as f:
        return f.read()
    except FileNotFoundError:
      raise FileNotFoundError("File not found!")
      return