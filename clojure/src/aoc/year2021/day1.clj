(ns aoc.year2021.day1
  (:require [aoc.utils :as utils]))

(defn puzzle-input  []
  (utils/intlist (utils/get-input 2021 1)))

(defn puzzle1 [input]
  (->>
   input
   (#(map vector % (rest %)))
   (map (fn [[a b]] (if (< a b) 1 0)))
   (reduce +)
   ))

(defn puzzle2 [input]
  (->>
   input
   (#(let [tail1 (rest %)
           tail2 (rest tail1)]
       (map vector % tail1 tail2)))
   (map #(apply + %))
   (puzzle1))
  
  )

(comment
  (puzzle1 [199
            200
            208
            210
            200
            207
            240
            269
            260
            263])
  (puzzle1 (puzzle-input))
  (puzzle2 [199
            200
            208
            210
            200
            207
            240
            269
            260
            263])
  (puzzle2 (puzzle-input)))