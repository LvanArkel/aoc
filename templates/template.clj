(ns aoc.year{year}.day{day}
  (:require [aoc.utils :as utils]))

(defn parse-input [input]
  input)

(defn puzzle-input [] (parse-input (utils/get-input {year} {day})))
(defn test-input [] (parse-input ""))

(defn puzzle1 [input]
  :todo)

(defn puzzle2 [input]
  :todo)

(comment
  ;;Room for tests
  (puzzle1 (test-input))
  (puzzle1 (puzzle-input));; Result
  ;;Room for tests
  (puzzle2 (test-input))
  (puzzle2 (puzzle-input));; Result
  )