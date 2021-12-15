(ns aoc.year2021.day14
  (:require [aoc.utils :as utils]
            [clojure.string :as string]))

(defn make-lookup [instrs]
  (reduce #(assoc-in %1 [(first %2) (second %2)] (last %2)) {} instrs))


(defn parse-input [input]
  (let [[polymer instrs] (string/split input #"(\r?\n){2}")]
    {:polymer polymer
     :instrs (reduce (fn [m tup] (assoc m (first tup) (second tup))) {}
                   (utils/split-and-patmatch instrs #"\r?\n" #"(\w\w) -> (\w)"))}))

(defn puzzle-input [] (parse-input (utils/get-input 2021 14)))
(defn test-input [] (parse-input "NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"))

(defn pol->freq [pol]
  (reduce (fn [m i] (update m (subs pol i (+ 2 i))
                            #(if (nil? %) 1 (inc %))))
          {}
          (range (dec (count pol)))))

(defn squeeze [grp instrs]
  (let [letr (get instrs grp)]
    [(str (first grp) letr)
     (str letr (second grp))]))

(defn grow [pol instrs]
  (apply merge-with +
         (apply concat (for [[k v] pol] (let [[a b] (squeeze k instrs)]
                                          [{a v}  {b v}])))))

(defn calc-amount [pairs fs ls]
  (->> (for [[k v] pairs] [{(first k) v} {(second k) v}])
       (apply concat)
       (apply merge-with +)
       (#(update % fs inc))
       (#(update % ls inc))
       (reduce-kv #(assoc %1 %2 (/ %3 2)) {})
       vals
       (#(let [ma (apply max %)
               mi (apply min %)]
           (- ma mi)))))

(defn run-sim [input n]
  (calc-amount
   ((apply comp (repeat n #(grow % (:instrs input))))
    (pol->freq (:polymer input)))
   (first (:polymer input))
   (last (:polymer input))))

(defn puzzle1 [input]
  (run-sim input 10))

(defn puzzle2 [input]
  (run-sim input 40))

(comment
  ;;Room for tests
  (puzzle1 (test-input))
  (puzzle1 (puzzle-input));; 2891
  ;;Room for tests
  (puzzle2 (test-input))
  (puzzle2 (puzzle-input));; 4607749009683
  )