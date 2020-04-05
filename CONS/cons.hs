import System.Environment
import Data.List
import Data.Maybe

fastaToList :: [Char] -> [[Char]]
fastaToList [] = []
fastaToList xs = filter (/=[]) ([filter (`elem` ['A', 'G', 'T', 'C']) x] ++ fastaToList z)
    where (x, y) = break ('>'==) xs
          z = if null y then [] else tail y

profileRow :: [Char] -> Char -> [Int]
profileRow [] c = []
profileRow (x:xs) c = [y] ++ profileRow xs c
    where y = if x == c then 1 else 0

addTuples :: Num a => (a, a) -> a
addTuples (x, y) = x + y

addTwoRows :: [Int] -> [Int] -> [Int]
addTwoRows xs ys = map addTuples (zip xs ys)

addProfileRows :: [[Char]] -> Char -> [Int]
addProfileRows [x] c = profileRow x c
addProfileRows (x:xs) c = addTwoRows (profileRow x c) (addProfileRows xs c)

argmax :: (Ord a) => [a] -> Int
argmax xs = fromJust $ elemIndex (maximum xs) xs

dnaIndexToDna :: Int -> Char
dnaIndexToDna x = ['A', 'C', 'G', 'T'] !! x 

profileToDnaIndex :: [[Int]] -> [Char]
profileToDnaIndex [[], [], [], []] = []
profileToDnaIndex m = dnaIndexToDna (argmax (map head m)) : profileToDnaIndex (map tail m)

formattedPrint :: [Int] -> [Char]
formattedPrint [] = ""
formattedPrint x = (intercalate " " y) ++ "\n"
    where y = map (show) x

main = do
    [arg] <- getArgs
    input <- readFile arg
    let dnas = fastaToList input
    let matrix = [addProfileRows dnas 'A'] ++ [addProfileRows dnas 'C'] ++ [addProfileRows dnas 'G'] ++ [addProfileRows dnas 'T']
    putStr $ profileToDnaIndex matrix
    putStr "\n"
    putStr $ "A: " ++ formattedPrint (matrix !! 0)
    putStr $ "C: " ++ formattedPrint (matrix !! 1)
    putStr $ "G: " ++ formattedPrint (matrix !! 2)
    putStr $ "T: " ++ formattedPrint (matrix !! 3)
