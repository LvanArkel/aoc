(ns aoc.year2021.day12
  (:require [aoc.utils :as utils]))

(defn parse-input [input]
  (reduce (fn [mp [s d]]
            (if (contains? mp s)
              (update mp s #(conj % d))
              (assoc mp s [d])))
          {}
          (reduce (fn [ls [_ s d]]
                    (conj ls [s d] [d s]))
                  []
                  (utils/patmatch-lines input #"(\w+)-(\w+)"))))

(def puzzle-input (parse-input (utils/get-input 2021 12)))
(def test-input (parse-input "start-A
start-b
A-c
A-b
b-d
A-end
b-end"))

(defn find-paths [graph node visited]
  (let [dests (graph node)
        small (Character/isLowerCase (get node 0))
        newv (if small (conj visited node) visited)]
    (if (= "end" node)
      (list (list node))
      (->> dests
           (remove #(contains? visited %))
           (map #(find-paths graph % newv))
           (apply concat)
           (map #(conj % node))))))

(defn find-paths2 [graph node visited second-visit]
  (let [dests (graph node)
        small (Character/isLowerCase (get node 0))
        newv (if small (conj visited node) visited)]
    (if (= "end" node)
      (list (list node))
      (concat
       (->> dests
            (remove #(contains? visited %))
            (map #(find-paths2 graph % newv second-visit))
            (apply concat)
            (map #(conj % node)))
       (when (not second-visit)
         (->> dests 
              (remove #(= "start" %))
              (map #(find-paths2 graph % newv true))
              (apply concat)
              (map #(conj % node))))))))

(defn puzzle1 [input]
  (count (find-paths input "start" #{"start"})))

(defn puzzle2 [input]
  (count (distinct (find-paths2 input "start" #{} false))))

(comment
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 puzzle-input);; 3510
  ;;Room for tests
  (puzzle2 test-input)
  (puzzle2 puzzle-input);; 122880
  )