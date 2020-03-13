import System.IO
import Data.List
import Data.Function
import Data.Maybe
import Data.Ord

fastaToList :: [Char] -> [[Char]]
fastaToList [] = []
fastaToList xs = filter (/=[]) ([filter (`elem` ['A', 'G', 'T', 'C']) x] ++ fastaToList z)
    where (x, y) = break ('>'==) xs
          z = if null y then [] else tail y

isInEveryString :: [Char] -> [[Char]] -> Bool
isInEveryString x [] = True
isInEveryString y (x:xs) = if isInfixOf y x then isInEveryString y xs else False

everySubstringPossible :: [Char] -> [[Char]]
everySubstringPossible [x, y, z] = [[x, y, z]]
everySubstringPossible xs = [xs, (tail xs), (init xs)] ++ everySubstringPossible (tail xs) ++ everySubstringPossible (init xs)

findMatches :: [[Char]] -> [[Char]] -> [[Char]]
findMatches [] ys = []
findMatches (x:xs) ys = if isInEveryString x ys then [x] ++ findMatches xs ys else findMatches xs ys

everySubstringFromList :: [[Char]] -> [[Char]]
everySubstringFromList [x] = everySubstringPossible x
everySubstringFromList xs = (everySubstringPossible (head xs)) ++ everySubstringFromList (tail xs)

remove :: (Ord a) => Int -> [a] -> [a]
remove n xs = x ++ (tail y)
    where (x, y) = splitAt n xs

argmax :: (Ord a) => [a] -> Int
argmax xs = fromJust $ elemIndex (maximum xs) xs

argmaxByLength :: [[Char]] -> Int
argmaxByLength xs = argmax (map length xs)

sortByLength :: [[Char]] -> [[Char]]
sortByLength xs = reverse (sortBy (comparing length) xs)

-- Incomplete/Too slow
main = do
    inputs <- getContents
    let dnaStrings = fastaToList inputs
    let substrings = everySubstringFromList dnaStrings
    let matches = findMatches substrings dnaStrings
    print $ substrings !! 0
