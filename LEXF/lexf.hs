import System.IO
import System.Environment
import Data.List

main = do
    (filename:_) <- getArgs
    dataset <- readFile filename
    let [s, ni] = lines dataset
    let n = read ni :: Int
    let a = filter (/=' ') s
    putStrLn $ (intercalate "\n" . sequence . take n . repeat) a