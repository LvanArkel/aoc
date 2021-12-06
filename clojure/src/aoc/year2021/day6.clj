(ns aoc.year2021.day6
  (:require [aoc.utils :as utils]))

(defn parse-input [input]
  (-> input utils/csvint frequencies))

(def puzzle-input (parse-input (utils/get-input 2021 6)))
(def test-input (parse-input "3,4,3,1,2"))

(defn puzzle1 [input n]
  (loop [timer n fish input]
    (if (> timer 0)
      (recur
       (dec timer)
       (let [new-fish (reduce #(if (some? (get fish (inc %2)))
                                 (assoc %1 %2 (get fish (inc %2)))
                                 %1) {} (range 0 8))]
         (if (some? (get fish 0))
           (-> new-fish
               (assoc 8 (get fish 0))
               (update 6 #(+ (if (some? %) % 0) (get fish 0))))
           new-fish))
       )
      (apply + (vals fish)))))

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