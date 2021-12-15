(ns aoc.year2021.day13
  (:require [aoc.utils :as utils]
            [clojure.string :as string]))

(defn parse-input [input]
  (let [[holes instr] (string/split input #"(\r?\n){2}")]
    {:holes (set (map (comp vec (fn [x] (map #(Integer/parseInt %) x)) rest) (utils/patmatch-lines holes #"(\d+),(\d+)")))
     :instr (map (comp (fn [[c v]] [c (Integer/parseInt v)]) rest) (utils/patmatch-lines instr #"fold along (x|y)=(\d+)"))}))

(def puzzle-input (parse-input (utils/get-input 2021 13)))
(def test-input (parse-input "6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"))

(defn fold-paper [holes instr]
  (let [pred (if (= "x" (first instr))
               (fn [[x _]] (> x (second instr)))
               (fn [[_ y]] (> y (second instr))))
        change (if (= "x" (get instr 0))
                 (fn [[x y] fe] [(- fe (- x fe)) y])
                 (fn [[x y] fe] [x (- fe (- y fe))]))]
    (set (map #(if (pred %) (change % (second instr)) %) holes))))

(defn sizes [holes]
  [(apply max (map first holes))
   (apply max (map second holes))])

(defn puzzle1 [input]
  (count (fold-paper (input :holes) (first (input :instr)))))

(defn puzzle2 [input]
  (let [holes (reduce fold-paper (input :holes) (input :instr))
        [xmax ymax] (sizes holes)]
    (string/join
     "\n"
     (map string/join
          (reduce (fn [paper [x y]] (assoc-in paper [y x] \#))
                  (vec (repeat (inc ymax) (vec (repeat (inc xmax) \.))))
                  holes)))))

(comment
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 puzzle-input);; 729
  ;;Room for tests
  (println (puzzle2 test-input))
  (println (puzzle2 puzzle-input));; RGZLBHFP
  )