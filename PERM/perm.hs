import System.Environment
import Data.List

factorial :: Integer -> Integer
factorial 1 = 1
factorial n = n * factorial (n-1)

ntuple :: Integer -> [Integer]
ntuple 1 = [1]
ntuple n = [n] ++ ntuple (n-1)

formattedPrint :: [[Integer]] -> [Char]
formattedPrint [] = ""
formattedPrint (x:xs) = (intercalate " " y) ++ "\n" ++ (formattedPrint xs)
    where y = map (show) x

main = do
    [arg] <- getArgs
    let input = read arg :: Integer
    print $ factorial input
    putStr $ formattedPrint (permutations (ntuple input))
