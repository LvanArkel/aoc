(ns aoc.year2021.day2
  (:require [aoc.utils :as utils]))

(def puzzle-input (utils/split-and-patmatch (utils/get-input 2021 2) #"\n" #"(\w+)\s(\d+)"))
(def test-input (utils/split-and-patmatch "forward 5
down 5
forward 8
up 3
down 8
forward 2" #"\n" #"(\w+)\s(\d+)"))

(defn puzzle1 [input]
  (apply *
         (reduce (fn [[x y] [_ dir val]] 
                   (let [vali (Integer/parseInt val)]
                     (case dir
                       "forward" [(+ x vali) y]
                       "down" [x (+ y vali)]
                       "up" [x (- y vali)])))
                 [0 0] input)))

(defn puzzle2 [input]
  ((fn [[x y _]] (* x y))
         (reduce (fn [[x y aim] [_ dir val]]
                   (let [vali (Integer/parseInt val)]
                     (case dir
                       "forward" [(+ x vali) (+ y (* aim vali)) aim]
                       "down" [x y (+ aim vali)]
                       "up" [x y (- aim vali)])))
                 [0 0 0] input)))

(comment
  puzzle-input
  test-input
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 puzzle-input);; 2215080
  ;;Room for tests
  (puzzle2 test-input)
  (puzzle2 puzzle-input);; 1864715580

  )