import System.IO
import Data.List
import Data.Map
import Data.Maybe

takeEvery :: Int -> [a] -> [a]
takeEvery n [] = []
takeEvery n xs = y : takeEvery n ys
    where (y:ys) = drop (n-1) xs

dropSubstring :: [Char] -> [Char] -> [Char]
dropSubstring ys xs = if isPrefixOf ys xs then drop (length ys) xs else (head xs):dropSubstring ys (tail xs)

exons :: [[Char]] -> [Char] -> [Char]
exons [] xs = xs
exons ys xs = dropSubstring (head ys) (exons (tail ys) xs)

dnaToRna :: [Char] -> [Char]
dnaToRna xs = 
    let repl 'T' = 'U'
        repl   c = c
    in Data.List.map repl xs

rnaToProt :: [Char] -> Data.Map.Map [Char] [Char] -> [Char]
rnaToProt xs rm = if p == "Stop" then "" else p ++ rnaToProt (drop 3 xs) rm
    where p = fromMaybe "Stop" (Data.Map.lookup (take 3 xs) rm)  

main = do
    input <- getContents
    let rna_map = Data.Map.fromList [("UUU", "F"), ("CUU", "L"), ("AUU", "I"), ("GUU", "V"), ("UUC", "F"), ("CUC", "L"), ("AUC", "I"), ("GUC", "V"), ("UUA", "L"), ("CUA", "L"), ("AUA", "I"), ("GUA", "V"), ("UUG", "L"), ("CUG", "L"), ("AUG", "M"), ("GUG", "V"), ("UCU", "S"), ("CCU", "P"), ("ACU", "T"), ("GCU", "A"), ("UCC", "S"), ("CCC", "P"), ("ACC", "T"), ("GCC", "A"), ("UCA", "S"), ("CCA", "P"), ("ACA", "T"), ("GCA", "A"), ("UCG", "S"), ("CCG", "P"), ("ACG", "T"), ("GCG", "A"), ("UAU", "Y"), ("CAU", "H"), ("AAU", "N"), ("GAU", "D"), ("UAC", "Y"), ("CAC", "H"), ("AAC", "N"), ("GAC", "D"), ("UAA", "Stop"), ("CAA", "Q"), ("AAA", "K"), ("GAA", "E"), ("UAG", "Stop"), ("CAG", "Q"), ("AAG", "K"), ("GAG", "E"), ("UGU", "C"), ("CGU", "R"), ("AGU", "S"), ("GGU", "G"), ("UGC", "C"), ("CGC", "R"), ("AGC", "S"), ("GGC", "G"), ("UGA", "Stop"), ("CGA", "R"), ("AGA", "R"), ("GGA", "G"), ("UGG", "W"), ("CGG", "R"), ("AGG", "R"), ("GGG", "G")]
    let s = takeEvery 2 (lines input)
    print $ rnaToProt (dnaToRna $ exons (drop 1 s) (head s)) rna_map
    