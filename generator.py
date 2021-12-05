languages = {"clojure": {"extension": "clj", "dir": "clojure/src/aoc/year"},
            "python": {"extension": "py", "dir": "python/"}}

template_path = "templates/template."

if __name__ == "__main__":
  print("languages: ", languages.keys())
  language_i = input("Select a programming language: ")
  while language_i not in languages.keys():
    language_i = input("Language doesn't exist, try again: ")
  language = languages[language_i]
  year = int(input("Select a year: "))
  day = int(input("Select a day: "))
  with open(template_path + language["extension"]) as f_temp:
    template = f_temp.read().format(year = year, day = day)
    with open(language["dir"] + f"{year}/day{day}.{language['extension']}", 'x') as f_write:
      f_write.write(template)
