(ns aoc.matrixutils)

(defn transpose [matrix]
  (apply map list matrix))