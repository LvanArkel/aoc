(ns aoc.year2015.day2
  (:require [aoc.utils :as utils]))

(defn parse-input [input]
  (utils/split-and-patmatch
   input
   #"\n"
   #"(\d+)x(\d+)x(\d+)"))

(def puzzle-input (parse-input (utils/get-input 2015 2)))
(def test-input (parse-input "2x3x4\n"))
(def test-input2 (parse-input "1x1x10\n"))

(defn handler1 [line]
  (let [l (Integer/parseInt (get line 1))
        w (Integer/parseInt (get line 2))
        h (Integer/parseInt (get line 3))
        a (* l w)
        b (* w h)
        c (* h l)]
    (+ (* 2 (+ a b c)) (min a b c))))

(defn handler2 [line]
  (let [l (Integer/parseInt (get line 1))
        w (Integer/parseInt (get line 2))
        h (Integer/parseInt (get line 3))]
    (+ (* l w h) (* 2 (- (+ l w h) (max l w h))))))

(defn puzzle1 [input]
  (apply + (map handler1 input)))

(defn puzzle2 [input]
  (apply + (map handler2 input)))

(comment
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 test-input2)
  (puzzle1 puzzle-input);; 1586300
  ;;Room for tests
  (puzzle2 test-input)
  (puzzle2 puzzle-input);; 3737498
  )