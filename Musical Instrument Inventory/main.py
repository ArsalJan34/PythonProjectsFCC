class MusicalInstrument:
  def __init__(self, name, instrument_type):
      self.name = name
      self.intrument_type = instrument_type

  def play(self):
     print(f"The {self.name} is fun to play!")
  def music_fact(self):
     return f"The {self.name} is part of the {self.intrument_type} family of instrument"

instrument_1 = MusicalInstrument("Oboe", "WoodWind")
instrument_2 = MusicalInstrument("Trumpet", "Brass")

instrument_1.play()
print(instrument_1.music_fact())

instrument_2.play()
print(instrument_2.music_fact())
