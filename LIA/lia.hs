import System.IO
import System.Environment
import Data.List
import Data.List.Split
import Data.Function

-- Un parent Aa Bb peut donner quatre quatre gamètes: AB Ab aB ab, donc toutes les combinaisons possibles,
-- chacun avec 1/4 d'arriver. Donc la chance d'avoir une descendance Aa Bb est de 1/4 peu importe le deuxième
-- parent, car le premier peut le compléter. 
--
-- http://www.cs.cornell.edu/~ginsparg/physics/INFO295/l2.pdf

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n-1)

comb :: (Integral a) => a -> a -> a
comb n k = (factorial n) `div` ((factorial k) * (factorial (n-k)))

binomialProb :: (Integral a) => a -> a -> a -> a
binomialProb n r k = sum $ map (\i -> comb n i * r^(n-i)) [k..n]

prob :: (Integral a) => a -> a -> Double
prob n k = fromIntegral (binomialProb k 3 n) / (4^k) -- 1 - 1/4 = 3/4

main = do
    (filename:_) <- getArgs
    dataset <- readFile filename
    let [k, n] = map read (words dataset) :: [Integer]
    print $ prob n (2^k)
