(ns aoc.year2021.day11
  (:require [aoc.utils :as utils]
            [clojure.set :refer [union]]))

(defn parse-input [input]
  (vec (map (comp vec utils/digitseq) (utils/split-lines input))))

(def puzzle-input (parse-input (utils/get-input 2021 11)))
(def test-input (parse-input "5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"))

(def coords (apply concat (map (fn [r] (map (fn [c] [r c]) (range 10)))
                               (range 10))))

(defn lookup [grid [r c]]
  (get (get grid r) c))

(defn neighbours [[r c]]
  (remove #(or (and (= r (first %))
                    (= c (second %)))
               (< (first %) 0)
               (< (second %) 0)
               (>= (first %) 10)
               (>= (second %) 10))
          
          (apply concat
                 (map (fn [nr] (map (fn [nc] [(+ r nr) (+ c nc)])
                                    (range -1 2)))
                      (range -1 2)))))

(defn flash [grid coord]
  (loop [open (list coord)
         grid grid
         n 0
         flashed #{}]
    (cond
      (empty? open)
      [grid n flashed]

      (< (lookup grid (first open)) 9)
      (recur (rest open)
             (update-in grid (first open) inc)
             n
             flashed)
      
      :else
      (recur (concat (rest open) (neighbours (first open)))
             (assoc-in grid (first open) 0)
             (inc n)
             (conj flashed (first open))))))

(defn step [cave _]
  (let [result (reduce
                (fn [{:keys [grid n flashed stepflash]} coord]
                  (let [digit (lookup grid coord)]
                    (cond
                      (< digit 9)
                      {:grid (update-in grid coord inc)
                       :n n
                       :stepflash stepflash
                       :flashed flashed}
                      :else
                      (let [[ngrid delta nflashed] (flash
                                                    grid
                                                    coord)]
                        {:grid ngrid
                         :n (+ n delta)
                         :stepflash (+ stepflash delta)
                         :flashed (union flashed nflashed)}))))
                (assoc cave :flashed #{})
                coords)
        flashed (:flashed result)
        grid (:grid result)
        n (:n result)
        stepflash (:stepflash result)]
    {:grid (reduce #(assoc-in %1 %2 0) grid flashed)
     :n n
     :stepflash stepflash}))

(defn puzzle1 [input n]
  ((reduce step {:grid input :n 0 :stepflash 0} (range n)) :n))

(defn puzzle2 [input]
  (reduce #(let [result (step (assoc %1 :stepflash 0) %2)]
             (cond
               (= (result :stepflash) 100)
               (reduced (inc %2))
               :else
               result))
          {:grid input :n -1}
          (range)))

(comment
  ;;Room for tests
  (step (step {:grid test-input :n 0} 0) 0)
  (puzzle1 test-input 10)
  (puzzle1 puzzle-input 100);; 1743
  ;;Room for tests
  (puzzle2 test-input)
  (puzzle2 puzzle-input);; 364
  )