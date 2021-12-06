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

(defn split-lines [input] (string/split-lines input))

(defn split-and-patmatch [input split pattern] 
  (map #(re-find (re-matcher pattern %)) (string/split input split)))


;;Make file from template
(defn makefile [year day]
  (let [contents (format (slurp (io/reader template-path))
                     year day year day)]
    (with-open [wrtr (io/writer (string/join "/" [file-path (str "year" year) (str "day" day ".clj")]))]
      (.write wrtr contents))))

(comment (makefile 2021 4))