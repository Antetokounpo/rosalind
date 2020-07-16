import System.IO
import System.Environment
import Data.List
import Data.List.Split
import Data.Function

fastaToGroups :: [String] -> [[String]]
fastaToGroups x = groupBy ((==) `on` (\y -> head y == '>')) x

groupsToMap :: [[String]] -> [(String, String)]
groupsToMap [] = []
groupsToMap (x:y:xs) = (head x, concat y) : groupsToMap xs

fastaToMap :: String -> [(String, String)]
fastaToMap = groupsToMap . fastaToGroups . lines

mapToDnaList :: [(String, String)] -> [String]
mapToDnaList = map snd

fastaToDnaList :: String -> [String]
fastaToDnaList = mapToDnaList . fastaToMap


data Nucleobase = A | T | G | C deriving(Show, Read)
instance Eq Nucleobase where
    A == G = True
    G == A = True
    T == C = True
    C == T = True
    _ == _ = False

countTransitions :: String -> String -> Double
countTransitions [] _ = 0
countTransitions (x:xs) (y:ys)
    | (read [x] :: Nucleobase) == (read [y] :: Nucleobase) = 1 + countTransitions xs ys
    | otherwise = countTransitions xs ys

countTranversions :: String -> String -> Double
countTranversions [] _ = 0
countTranversions (x:xs) (y:ys)
    | x == y = countTranversions xs ys
    | (read [x] :: Nucleobase) /= (read [y] :: Nucleobase) = 1 + countTranversions xs ys
    | otherwise = countTranversions xs ys

getRatio :: String -> String -> Double
getRatio x y = (countTransitions x y)/(countTranversions x y)

main = do
    (filename:_) <- getArgs
    dataset <- readFile filename
    let [x, y] = fastaToDnaList dataset
    print $ getRatio x y