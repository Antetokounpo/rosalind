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

main = do
    (filename:_) <- getArgs
    dataset <- readFile filename
    print dataset