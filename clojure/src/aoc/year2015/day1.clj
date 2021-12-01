(ns aoc.year2015.day1
  (:require [aoc.utils :as utils]))

(defn puzzle-input []
  (utils/get-input 2015 1))

(defn delta-floor [c]
  (if (= c \()
    1
    -1))

(defn puzzle1 [input]
  (->>
   input
   (map delta-floor)
   (reduce +)))

(defn puzzle2 [input]
  (loop [i 0 floor 0 lst input]
    (if (< floor 0)
      i
      (recur (inc i) (+ floor (delta-floor (first lst))) (rest lst)))))


(comment
  (puzzle1 "(())")
  (puzzle1 "()()")
  (puzzle1 "))(((((")
  (puzzle1 (puzzle-input));;74
  (puzzle2 (puzzle-input));;1795
  )