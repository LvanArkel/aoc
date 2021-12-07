(ns aoc.year2021.day7
  (:require [aoc.utils :as utils]))

(defn parse-input [input]
  (utils/csvint input))

(def puzzle-input (parse-input (utils/get-input 2021 7)))
(def test-input (parse-input "16,1,2,0,4,2,7,1,2,14"))

(defn puzzle1 [input]
  (let [minimum (apply min input)
        maximum (apply max input)]
    (apply min 
           (reduce 
            (fn [ls n]
              (conj ls
                    (apply + 
                           (map #(Math/abs (- % n)) 
                                input)))) 
            [] (range minimum maximum)))))

(defn puzzle2 [input]
  (let [minimum (apply min input)
        maximum (apply max input)
        costs (vec (reductions + (range (inc maximum))))]
    (apply min 
           (reduce 
            (fn [ls n]
              (conj ls 
                    (apply + 
                           (map #(get costs (Math/abs (- % n))) input))))
            [] (range minimum maximum)))))

(comment
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 puzzle-input);; 323647
  ;;Room for tests
  (puzzle2 test-input)
  (puzzle2 puzzle-input);; 87640209
  )