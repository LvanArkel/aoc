(ns aoc.year2021.day9
  (:require [aoc.utils :as utils]))

(defn parse-input [input]
  (map (fn [line] (vec (map #(- (int %) 48) line)))
       (utils/split-lines input)))

(def puzzle-input (parse-input (utils/get-input 2021 9)))
(def test-input (parse-input "2199943210
3987894921
9856789892
8767896789
9899965678"))

(defn lookup [grid [r c]]
  (-> grid
      (nth r)
      (nth c)))

(defn neighbours [[r c] width height]
  (filter
   (fn [[r c]] (and (>= r 0)
                    (>= c 0)
                    (< r height)
                    (< c width)))
   [[(dec r) c]
    [(inc r) c]
    [r (dec c)]
    [r (inc c)]]))

(defn find-basin [coord grid width height]
  (loop [visited #{} open [coord]]
    (if (empty? open)
      (count visited)
      (let [adjacent (filter #(and (not (contains? visited %))
                                   (< (lookup grid %) 9))
                             (neighbours (first open) width height))]
        (recur (conj visited (first open)) (concat (rest open) adjacent))))))

(defn find-low-row [rows]
  (map (fn [row]
         (let [rshift (cons 10 row)
               lshift (rest (conj row 10))]
           (map #(and (< %2 %1) (< %2 %3)) lshift row rshift)))
       rows))

(defn find-low-points [input]
  (let [rows (find-low-row input)
        cols (utils/transpose (find-low-row (utils/transpose input)))]
    (apply concat (map-indexed (fn [r col] (map #(vector r %) col)) (map (fn [rr cr] (keep-indexed (fn [c [x y]] (if (and x y) c)) (map (fn [r c] [r c]) rr cr))) rows cols)))))

(defn puzzle1 [input]
  (->> input
       find-low-points
       (map #(lookup input %))
       (map inc)
       (apply +)))

(defn puzzle2 [input]
  (let [width (count (first input))
        height (count input)]
    (->>
     input
     find-low-points
     (map #(find-basin % input width height))
     (sort >)
     (take 3)
     (apply *))))

(comment
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 puzzle-input);; 554
  ;;Room for tests
  (puzzle2 test-input)
  (puzzle2 puzzle-input);; 1017792
  )