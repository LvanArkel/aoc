(ns aoc.year2021.day10
  (:require [aoc.utils :as utils]))

(defn parse-input [input]
  (utils/split-lines input))

(def puzzle-input (parse-input (utils/get-input 2021 10)))
(def test-input (parse-input "[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"))

(def open-to-close {\( \) \{ \} \[ \] \< \>})
(def syntax-points {\) 3 \] 57 \} 1197 \> 25137})
(def closing-score {\( 1 \[ 2 \{ 3 \< 4})

(defn reduce-line [line]
  (loop [stack (list) program line]
    (cond
      (empty? program)
      0

      (contains? #{\( \[ \{ \<} (first program))
      (recur (conj stack (first program)) (rest program))

      (= (open-to-close (peek stack)) (first program))
      (recur (pop stack) (rest program))

      :else
      (syntax-points (first program)))))

(defn make-stack [line]
  (loop [stack '() program line]
    (cond 
      (empty? program)
      stack
      
      (contains? #{\( \[ \{ \<} (first program))
      (recur (conj stack (first program)) (rest program))
      
      :else
      (recur (pop stack) (rest program)))))

(defn puzzle1 [input]
  (reduce + (map reduce-line input)))

(defn puzzle2 [input]
  (->> input
       (filter #(= 0 (reduce-line %)))
       (map make-stack)
       (map #(map closing-score %))
       (map (fn [score] (reduce #(+ (* 5 %1) %2) 0 score)))
       sort
       (#(let [cnt (count %)]
           (drop (quot cnt 2) %)))
       first))

(comment
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 puzzle-input);; 296535
  ;;Room for tests
  (make-stack "[({(<(())[]>[[{[]{<()<>>")
  (puzzle2 test-input)
  (puzzle2 puzzle-input);; 4245130838
  )