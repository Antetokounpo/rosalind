import System.IO
import System.Environment
import Data.List
import Data.Function

fib :: Int -> Integer
fib 1 = 1
fib 2 = 1
fib n = fib (n-1) + fib (n-2)

memoized_fib :: Int -> Integer
memoized_fib = (map fib [0..] !!)
    where fib 0 = 0
          fib 1 = 1
          fib n = memoized_fib (n-2) + memoized_fib (n-1)

nfib :: Int -> Integer
nfib 0 = 1
nfib 1 = 1
nfib n = a n + b n
    where a 1 = 0
          a n = nfib (n-2)
          b n = a (n-1)

xfib :: Int -> Int -> Integer
xfib _ 0 = 1
xfib _ 1 = 1
xfib m n = a n + b n
    where b n
            | n <= 0 = 0
            | n == 1 = 1
            | n == 2 = 0
            | otherwise = sum $ map b [(n-m)..(n-2)]
          a n = sum $ map b [(n-(m-1))..(n-1)]

mxfib :: Int -> Int -> Integer
mxfib _ 0 = 1
mxfib _ 1 = 1
mxfib m n = a n + b n                            -- a = nb d'adultes, b = nb de bébés
    where b n
            | n <= 0 = 0
            | otherwise = (map bx [0..] !!) n   -- memoisation
          bx 1 = 1
          bx 2 = 0
          bx n = sum $ map b [(n-m)..(n-2)]    
          a n = sum $ map b [(n-(m-1))..(n-1)]

-- 1 2 3 4 5 6 7  8  -> n
-- 1 0 1 1 1 2 2  3  -> bébé
-- 0 1 1 1 2 2 3  4  -> adulte
-- 1 1 2 2 3 4 5  7  -> total
-- 1 1 2 3 5 8 13 21 -> fib n
-- 0 0 0 1 2 4 8  14 -> diff total | fib n

-- On voit que le nombre de bébé à n correspond au nombre d'adultes à (n-1).
-- On voit aussi que le nombre d'adultes à n correspond à la somme du nombre de bébés à (n-1) et (n-2) OU au nombre total à (n-2)
-- m = 3 dans le cas illustré
-- Si on généralise la situation, le nombre d'adultes à n correspond au nombres de bébés à (n-1) jusqu'à (n-(m-1)), car ce sont les bébés qui ont grandi, mais qui ne sont pas morts
-- Le nombre de bébés à n correspond au nombres d'adultes à (n-1), ce qui est égal au nombre de bébés de (n-2) jusqu'à (n-m) comme démontré plus haut.

main = do
    (filename:_) <- getArgs
    dataset <- readFile filename
    let [n, m] = map (read) (words dataset) :: [Int]
    print $ mxfib m n