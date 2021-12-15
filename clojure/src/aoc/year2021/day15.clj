(ns aoc.year2021.day15
  (:require [aoc.utils :as utils]))

(defn parse-input [input]
  (->> input
       utils/split-lines
       (map (comp vec utils/digitseq))
       vec
       utils/make-matrix))

(defn puzzle-input [] (parse-input (utils/get-input 2021 15)))
(defn test-input [] (parse-input "1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"))

(defn in-bounds [[a b] w h]
  (and (>= a 0)
       (>= b 0)
       (< a w)
       (< b h)))

(defn neighbours [w h [a b]]
  (filter #(in-bounds % w h) [[(inc a) b]
                              [(dec a) b]
                              [a (inc b)]
                              [a (dec b)]]))

(defn get-score [m k]
  (get m k Integer/MAX_VALUE))

(defn get-d [grid [r c]]
  (let [height (count grid)
        width (count (first grid))
        raw (+ (get-in grid [(mod r height)
                             (mod c width)])
               (quot r height)
               (quot c width))]
    (if (> raw 9)
      (loop [val raw]
        (if (> val 9)
          (recur (- val 9))
          val))
      raw)
    ))

(defn astar [grid width height]
  (let [maxr (dec height)
        maxc (dec width)
        h (fn [[r c]] (+ (- maxr r) (- maxc c)))]
    (loop [openset #{[0 0]} 
           gScore {[0 0] 0} 
           fScore {[0 0] (h [0 0])}]
      (if (empty? openset)
        (gScore [maxr maxc])
        (let [current (first (sort-by #(get-score fScore %) openset))
              openset (disj openset current)]
          (if (= current [maxr maxc])
            (gScore current)
            (let [toRecord (->> current
                                (neighbours width height)
                                (map (fn [n] [n (+ (get-score gScore current) (get-d grid n))]))
                                (filter (fn [[n tgs]] (< tgs (get-score gScore n)))))]
              (recur (apply conj openset (map first toRecord))
                     (merge gScore (into {} toRecord))
                     (merge fScore (into {} (map (fn [[n tgs]] [n (+ tgs (h n))]) toRecord))))))
          )))))

(defn puzzle1 [input]
  (let [{:keys [matrix height width]} input]
    (astar matrix width height)))

(defn puzzle2 [input]
  (let [{:keys [matrix height width]} input]
    (astar matrix (* 5 width) (* 5 height))))

(comment
  (get-d [[8]] [0 2])
  ;;Room for tests
  (filter #(in-bounds % 10 10) (map (fn [i] [i (- 6 i)]) (range (inc 6))))
  (puzzle1 (test-input))
  (puzzle1 (puzzle-input));; 540
  ;;Room for tests
  (puzzle2 (test-input))
  (puzzle2 (puzzle-input));; 2879
  )