import System.IO
import System.Environment
import Data.List
import Data.List.Split
import Data.Function
import qualified Data.Map as Map

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


matchStrands :: Int -> String -> String -> String
matchStrands n x y
    | x == y = []
    | a `isPrefixOf` x = (take n y) ++ x
    | b `isSuffixOf` x = x ++ (drop $ length y - n) y
    | otherwise = matchStrands (n+1) x y
    where a = tails y !! n
          b = (reverse . inits) y !! n

matchStrandsList :: [String] -> String
matchStrandsList [x, y] = matchStrands 0 x y
matchStrandsList (x:xs) = matchStrandsList (y:z)
    where ys = map (matchStrands 0 x) xs
          y = minimumBy (compare `on` length) $ filter (not . null) ys
          n = case findIndex (==y) ys of Just n -> n
          z = delete (xs !! n) xs

main = do
    (filename:_) <- getArgs
    dataset <- readFile filename
    let dnaList = fastaToDnaList dataset
    print $ matchStrandsList dnaList
