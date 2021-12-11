(ns aoc.year2021.day8
  (:require [aoc.utils :as utils]
            [clojure.set :as set]))

(defn letter->digit [l]
  (- (int l) 97))

(defn parse-input [input]
  (map #(let [ls (map (fn [line] (->> line first (map letter->digit) vec)) %)]
          {:input (take 10 ls)
           :output (drop 10 ls)}) (utils/patmatch-lines-all input #"(\w+)")))


(def puzzle-input (parse-input (utils/get-input 2021 8)))
(def test-input (parse-input "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"))
(def test-input2 (parse-input "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"))

(defn permutations [s]
  (lazy-seq
   (if (seq (rest s))
     (apply concat (for [x s]
                     (map #(cons x %) (permutations (remove #{x} s)))))
     [s])))
(def perms (map vec (permutations (range 7))))

(def amt->num
  {2 [1]
   3 [7]
   4 [4]
   5 [2 3 5]
   6 [0 6 9]
   7 [8]})

(def num->seg
  {0 [0 1 2 4 5 6]
   1 [2 5]
   2 [0 2 3 4 6]
   3 [0 2 3 5 6]
   4 [1 2 3 5]
   5 [0 1 3 5 6]
   6 [0 1 3 4 5 6]
   7 [0 2 5]
   8 [0 1 2 3 4 5 6]
   9 [0 1 2 3 5 6]})

(def seg->num (set/map-invert num->seg))

(def segments (vals num->seg))

;;  0
;; 1 2 
;;  3
;; 4 5
;;  6

(defn puzzle1 [input]
  (apply +
         (map (fn [line]
                (->>
                 line
                 :output
                 (filter #(contains? #{2 3 4 7} (count %)))
                 count))
              input)))

(defn matches [digit]
  (let [d-size (count digit)
        segs (map num->seg (amt->num d-size))
        d-perms (permutations digit)]
    (fn [perm]
      (some
       (fn [seg]
         (some (fn [d-perm]
                 (every? true?
                         (map #(= (get perm %1) %2) seg d-perm))) d-perms)) segs))))

(defn find-permutation [digits]
  (reduce (fn [ps digit]
            (filter (matches digit) ps)) perms digits))

(defn invert-permutation [perm]
  (vec (map second (sort (keep-indexed (fn [i v] [v i]) perm)))))

(defn solve-digits [data]
  (let [in (:input data)
        out (:output data)
        perm (first (find-permutation in))
        p-inv (invert-permutation perm)]
    (reduce #(+ (* 10 %1) %2) 0 (map (fn [digit]
                                       (->> digit
                                            (map p-inv)
                                            sort
                                            vec
                                            seg->num)) out))))

(defn puzzle2 [input]
  (apply + (map solve-digits input)))


(comment
  (reduce-perms perms)
  ;;Room for tests
  (puzzle1 test-input)
  (puzzle1 test-input2)
  (puzzle1 puzzle-input);; 321
  ;;Room for tests
  perms
  (-> test-input2 first :input)
  (solve-digits (first test-input))
  ([3 4 0 5 6 1 2])
  (puzzle2 test-input2)
  (puzzle2 puzzle-input);; Result
  )