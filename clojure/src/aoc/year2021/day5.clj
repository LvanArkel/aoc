(ns aoc.year2021.day5
  (:require [aoc.utils :as utils]))

(defn parse-input [input]
  (map (fn [line] (vec (map #(Integer/parseInt %) (rest line)))) (utils/split-and-patmatch input #"\r?\n"
                                      #"(\d+),(\d+) -> (\d+),(\d+)")))

(def puzzle-input (parse-input (utils/get-input 2021 5)))
(def test-input (parse-input "0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"))

(defn create-set1 [input]
  (filter #(or (= (get % 0)
                  (get % 2)) 
               (= (get % 1)
                  (get % 3)))
          input))

(defn make-lines [input]
  (reduce
   (fn [coll [x1 y1 x2 y2]]
     (cond
       (= x1 x2)
       (let [miny (min y1 y2)
             maxy (max y1 y2)]
         (concat coll (map (fn [v] [x1 v]) (range miny (inc maxy)))))
       (= y1 y2)
       (let [minx (min x1 x2)
             maxx (max x1 x2)]
         (concat coll (map (fn [v] [v y1]) (range minx (inc maxx)))))
       :else
       (concat
        coll
        (let [xdir (if (< x1 x2) 1 -1)
              ydir (if (< y1 y2) 1 -1)]
          (map vector 
               (range x1 (+ x2 xdir) xdir)
               (range y1 (+ y2 ydir) ydir))))))
   '()
   input))

(defn reduce-map [input]
  (let [freqs (frequencies input)]
    (count (filter #(>= (get freqs %) 2) (keys freqs)))))

(defn puzzle1 [input]
  (-> input 
      create-set1
      make-lines
      reduce-map))

(defn puzzle2 [input]
  (-> input
      make-lines
      reduce-map))

(comment
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 puzzle-input);; 6666
  ;;Room for tests
  (puzzle2 test-input)
  (puzzle2 puzzle-input);; 19081
  )