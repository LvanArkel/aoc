(ns aoc.year2021.day3
  (:require [aoc.utils :as utils]))

(def puzzle-input (utils/split-lines (utils/get-input 2021 3)))
(def test-input (utils/split-lines "00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"))

(def gamma-map {\0 -1
                \1 1})

(defn puzzle1 [input]
  (->>
   input
   (apply map list)
   (map #(map gamma-map %))
   (map #(apply + %))
   (map #(if (> % 0) 1 0))
   ((fn [xs] [xs (map #(- 1 %) xs)]))
   (map (fn [xs] (reduce #(+ (* %1 2) %2) 0 xs)))
   (apply *)))

(defn oxcofilter [bytes f]
  (loop [i 0 nums bytes]
    (cond
      (= 1  (count nums))
      (first nums)

      (>= i (count (first nums)))
      (first nums)

      :else
      (let [total (apply + (map #(get % i) nums))
            tosave (if (f total 0) 1 -1)]
        (recur (inc i) (filter #(= (get % i) tosave) nums))))))

(defn puzzle2 [input]
  (->> input (map #(map gamma-map %))
       (map vec)
       ((fn [xs] [(oxcofilter xs <) (oxcofilter xs >=)]))
       (map #(replace {1 1 -1 0} %))
       (map #(reduce (fn [a x] (+ (* 2 a) x)) 0 %))
       (apply *)))

(comment
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 puzzle-input);; 3985686
  ;;Room for tests
  (puzzle2 test-input)
  (puzzle2 puzzle-input);; 2555739
  )