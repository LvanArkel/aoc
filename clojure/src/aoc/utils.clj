(ns aoc.utils
  (:require [clojure.java.io :as io]
            [clojure.string :as string]))

(def resource-root "C:/Users/lvana/Documents/Programming/aoc/inputs")
(def file-path "C:/Users/lvana/Documents/Programming/aoc/clojure/src/aoc")
(def template-path (str file-path "/template.clj"))

(defn- get-file [year filename]
  (io/reader (string/join "/" [resource-root (str year) filename])))

(defn get-input [year day]
  (slurp (get-file year (string/join ["day" (str day) ".txt"]))))

(defn intlist [input] (->> input string/split-lines (map #(Integer/parseInt %))))

(defn csvint [input] (map #(Integer/parseInt %) (string/split input #",")))

(defn digitseq [input] (map #(- (int %) 48) input))

(defn split-lines [input] (string/split-lines input))

(defn split-and-patmatch [input split pattern] 
  (map (comp rest #(re-find (re-matcher pattern %))) (string/split input split)))

(defn patmatch-lines [input pattern]
  (map #(re-find pattern %) (string/split-lines input)))

(defn patmatch-lines-all [input pattern]
  (map #(re-seq pattern %) (string/split-lines input)))

(defn make-matrix [matrix]
  {:matrix matrix
   :height (count matrix)
   :width (count (first matrix))})

;;Make file from template
(defn makefile [year day]
  (let [contents (format (slurp (io/reader template-path))
                     year day year day)]
    (with-open [wrtr (io/writer (string/join "/" [file-path (str "year" year) (str "day" day ".clj")]))]
      (.write wrtr contents))))

(defn transpose [matrix]
  (apply map vector matrix))