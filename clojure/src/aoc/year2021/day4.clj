(ns aoc.year2021.day4
  (:require [aoc.utils :as utils]
            [aoc.matrixutils :as mutils]
            [clojure.string :as string]))

(defn parse-card [card]
  {:numbers (map (fn [line] 
                   (map #(when-not (empty? %) (Integer/parseInt %)) 
                        (string/split (string/trim line) #"\s+"))) 
                 (string/split-lines card))
   :taken (vec (repeat 5 (vec (repeat 5 false))))})

(defn parse-input [input]
  (let [lines (string/split input #"\r?\n\r?\n")]
    {:numbers (utils/csvint (first lines))
     :cards (map parse-card (rest lines))}))

(def puzzle-input (parse-input (utils/get-input 2021 4)))
(def test-input (parse-input "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7"))

(defn has-row [card]
  (reduce #(or %1 %2) (map #(reduce (fn [a b] (and a b)) %) (card :taken))))

(defn has-col [card]
  (has-row (update card :taken mutils/transpose)))

(defn has-bingo [card]
  (or (has-row card) (has-col card)))

(defn place-number [card n]
  (let [numbers (card :numbers)
        cols (map #(.indexOf % n) numbers)
        row (first (keep-indexed #(when (not= -1 %2) %1) cols))
        col (get (vec cols) row)]
    (if (nil? row)
      card
      (update-in card [:taken row col] (constantly true)))))

(defn eval-card [card]
  (let [numbers (card :numbers)
        taken (card :taken)
        masked (map (fn [[ns ts]] (map #(if %2 0 %1) ns ts)) (map vector numbers taken))]
    (apply + (flatten masked))
    ))

(defn puzzle1 [input]
  (reduce (fn [cards n] 
            (let [newCards (map #(place-number % n) cards)
                  winner (first (keep-indexed #(when (has-bingo %2) %1) newCards))]
               (if (nil? winner)
                newCards
                (reduced (* n (eval-card (get (vec newCards) winner)))))))
          (:cards input) (:numbers input)))

(defn puzzle2 [input]
  (reduce (fn [cards n]
            (let [newCards (map #(place-number % n) cards)]
              (if (and (= 1 (count cards)) (has-bingo (first newCards)))
                (reduced (* n (eval-card (first newCards))))
                (remove has-bingo newCards))))
          (:cards input) (:numbers input)))

(comment
  (-> test-input :cards first (place-number 7))
  (has-row {:taken [[true true true true true]
                    [false false false true false]
                    [false false true false false]
                    [false true false false true]
                    [true true false false true]]})
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 puzzle-input);; 63552
  ;;Room for tests
  (puzzle2 test-input)
  (puzzle2 puzzle-input);; 9020
  )