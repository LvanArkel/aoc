(ns aoc.year2021.day6
  (:require [aoc.utils :as utils]))

(defn parse-input [input]
  (let [intlist (utils/csvint input)]
    (vec (map #(count (filter (fn [v] (= % v)) intlist)) (range 9)))))

(def puzzle-input (parse-input (utils/get-input 2021 6)))
(def test-input (parse-input "3,4,3,1,2"))

(defn puzzle1 [input n]
  (loop [timer n fish input]
    (if (> timer 0)
      (recur
       (dec timer)
       (conj (update (vec (rest fish)) 6 #(+ (first fish) %))
             (first fish)))
      (apply + fish))))

(defn puzzle2 [input]
  :todo)

(comment
  ;;Room for tests
  (puzzle1 test-input 18)
  (puzzle1 test-input 80)
  (puzzle1 puzzle-input 80);; 360761
  ;;Room for tests
  (puzzle1 test-input 256)
  (puzzle1 puzzle-input 256);; Result
  )