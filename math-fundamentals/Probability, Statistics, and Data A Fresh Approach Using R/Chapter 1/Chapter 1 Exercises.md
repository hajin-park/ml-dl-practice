Chapter 1 Exercises
================
Hajin Park
December 22, 2024

### 1.1 Let `x <- c(1,2,3)` and `y <- c(6,5,4)`. Predict what will happen when the following pieces of code are run. Check your answer.

##### (a) `x * 2`

Answer: **\[2, 4, 6\]**

Solution:

``` r
x <- c(1,2,3)
x * 2
```

    ## [1] 2 4 6

##### (b) `x * y`

Answer: **\[6, 10, 12\]**

Solution:

``` r
x <- c(1,2,3)
y <- c(6,5,4)
x * y
```

    ## [1]  6 10 12

##### (c) `x[1] * y[2]`

Answer: **5**

Solution:

``` r
x <- c(1,2,3)
y <- c(6,5,4)
x[1] * y[2]
```

    ## [1] 5

### 1.2 Let `x <- c(1,2,3)` and `y <- c(6,5,4)`. What is the value of x after each of the following commands? (Assume that each part starts with the values of x and y given above.)

##### (a) `x + x`

Answer: **2, 4, 6**

Solution:

``` r
x <- c(1,2,3)
x + x
```

    ## [1] 2 4 6

##### (b) `x <- x + x`

Answer: **x = \[2, 4, 6\]**

Solution:

``` r
x <- c(1,2,3)
x <- x + x
x
```

    ## [1] 2 4 6

##### (c) `y <- x + x`

Answer: **2, 4, 6**

Solution:

``` r
x <- c(1,2,3)
y <- c(6,5,4)
y <- x + x
y
```

    ## [1] 2 4 6

##### (d) `x <- x + 1`

Answer: **2, 3, 4**

Solution:

``` r
x <- c(1,2,3)
x <- x + 1
x
```

    ## [1] 2 3 4

### 1.3 Determine the values of the vector `vec` after each of the following commands is run.

##### (a) `vec <- 1:10`

Answer: **1, 2, 3, 4, 5, 6, 7, 8, 9, 10**

Solution:

``` r
vec <- 1:10
vec
```

    ##  [1]  1  2  3  4  5  6  7  8  9 10

##### (b) `vec <- 1:10 * 2`

Answer: **2, 4, 6, 8, 10, 12, 14, 16, 18, 20**

Solution:

``` r
vec <- 1:10 * 2
vec
```

    ##  [1]  2  4  6  8 10 12 14 16 18 20

##### (c) `vec <- 1:10^2`

Answer: **1, 4, 9, 16, 25, 36, 49, 64, 81, 100**

Solution:

``` r
vec <- 1:10^2
vec
```

    ##   [1]   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18
    ##  [19]  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36
    ##  [37]  37  38  39  40  41  42  43  44  45  46  47  48  49  50  51  52  53  54
    ##  [55]  55  56  57  58  59  60  61  62  63  64  65  66  67  68  69  70  71  72
    ##  [73]  73  74  75  76  77  78  79  80  81  82  83  84  85  86  87  88  89  90
    ##  [91]  91  92  93  94  95  96  97  98  99 100

##### (d) `vec <- 1:10 + 1`

Answer: **2, 3, 4, 5, 6, 7, 8, 9, 10, 11**

Solution:

``` r
vec <- 1:10 + 1
vec
```

    ##  [1]  2  3  4  5  6  7  8  9 10 11

##### (e) `vec <- 1:(10 * 2)`

Answer: **1, 2, …, 20**

Solution:

``` r
vec <- 1:(10 * 2)
vec
```

    ##  [1]  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20

##### (f) `vec <- rep(c(1,1,2), times = 2)`

Answer: **1, 1, 2, 1, 1, 2**

Solution:

``` r
vec <- rep(c(1,1,2), times = 2)
vec
```

    ## [1] 1 1 2 1 1 2

##### (g) `vec <- seq(from = 0, to = 10, length.out = 5)`

Answer: **1, 2, 3, 4, 5**

Solution:

``` r
vec <- seq(from = 0, to = 10, length.out = 5)
vec
```

    ## [1]  0.0  2.5  5.0  7.5 10.0

### 1.4 In this exercise, you will graph the function $f(p) = p(1 - p)$ for $p \in [0, 1]$.

##### (a) Use `seq` to create a vector `p` of numbers from $0$ to $1$ spaced by $0.2$.

Solution:

``` r
p <- seq(from = 0, to = 1, length.out = 6)
p
```

    ## [1] 0.0 0.2 0.4 0.6 0.8 1.0

##### (b) Use `plot` to plot `p` in the `x` coordinate and $p(1-p)$ in the `y` coordinate. Read the help page for `plot` and experiment with the `type` argument to find a good choice for this graph.

Solution:

``` r
p <- seq(from = 0, to = 1, length.out = 6)
y <- p * (1 - p)
plot(p, y)
```

![](test_files/figure-gfm/1.4b%20Solution-1.png)<!-- -->

##### (c) Repeat, but with creating a vector `p` of numbers from $0$ to $1$ spaced by $0.01$.

Solution:

``` r
p <- seq(from = 0, to = 1, length.out = 11)
y <- p * (1 - p)
plot(p, y)
```

![](test_files/figure-gfm/1.4c%20Solution-1.png)<!-- -->

### 1.5 Use R to calculate the sum of the squares of all numbers from $1$ to $100$: $1^2 + 2^2 + \dots + 99^2 + 100^2$

Solution:

``` r
x <- 1:100
sum(x * x)
```

    ## [1] 338350

### 1.6 Let `x` be the vector obtained by running the R command `x <- seq(from = 10, to = 30, by = 2)`.

##### (a) What is the length of `x`? (By length, we mean the number of elements in the vector. This can be obtained using the `str` function or the `length` function.)

Answer: **11**

Solution:

``` r
x <- seq(from = 10, to = 30, by = 2)
length(x)
```

    ## [1] 11

##### (b) What is `x[2]`?

Answer: **12**

Solution:

``` r
x <- seq(from = 10, to = 30, by = 2)
x[2]
```

    ## [1] 12

##### (c) What is `x[1:5]`?

Answer: **10, 12, 14, 16, 18**

Solution:

``` r
x <- seq(from = 10, to = 30, by = 2)
x[1:5]
```

    ## [1] 10 12 14 16 18

##### (d) What is `x[1:3*2]`?

Answer: **10, 12, 14, 16, 18, 20**

Solution:

``` r
x <- seq(from = 10, to = 30, by = 2)
x[1:3*2]
```

    ## [1] 12 16 20

##### (e) What is `x[1:(3*2)]`?

Answer: **10, 12, 14, 16, 18, 20**

Solution:

``` r
x <- seq(from = 10, to = 30, by = 2)
x[1:(3*2)]
```

    ## [1] 10 12 14 16 18 20

##### (f) What is `x > 25`?

Answer: **FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, FALSE, TRUE,
TRUE, TRUE**

Solution:

``` r
x <- seq(from = 10, to = 30, by = 2)
x > 25
```

    ##  [1] FALSE FALSE FALSE FALSE FALSE FALSE FALSE FALSE  TRUE  TRUE  TRUE

##### (g) What is `x[x > 25]`?

Answer: **26, 28, 30**

Solution:

``` r
x <- seq(from = 10, to = 30, by = 2)
x[x > 25]
```

    ## [1] 26 28 30

##### (h) What is `x[-1]`?

Answer: **12, 14, 16, 18, 20, 22, 24, 26, 28, 30**

Solution:

``` r
x <- seq(from = 10, to = 30, by = 2)
x[-1]
```

    ##  [1] 12 14 16 18 20 22 24 26 28 30

##### (i) What is `x[-1:-3]`?

Answer: **16, 18, 20, 22, 24, 26, 28, 30**

Solution:

``` r
x <- seq(from = 10, to = 30, by = 2)
x[-1:-3]
```

    ## [1] 16 18 20 22 24 26 28 30

### 1.7 R has a built-in vector `rivers` which contains the lengths of major North American rivers.

##### (a) Use `?rivers` to learn about the data set.

Solution:

``` r
?rivers
```

##### (b) Find the mean and standard deviation of the rivers data using the base R functions `mean` and `sd`.

Solution:

``` r
x <- rivers
mean(x)
```

    ## [1] 591.1844

``` r
sd(x)
```

    ## [1] 493.8708

##### (c) Make a histogram `hist` of the rivers data.

Solution:

``` r
x <- rivers
hist(x, plot = TRUE)
```

![](test_files/figure-gfm/1.7c%20Solution-1.png)<!-- -->

##### (d) Get the five number summary (`summary`) of rivers data.

Solution:

``` r
summary(rivers)
```

    ##    Min. 1st Qu.  Median    Mean 3rd Qu.    Max. 
    ##   135.0   310.0   425.0   591.2   680.0  3710.0

##### (e) Find the longest and shortest lengths of rivers in the set.

Solution:

``` r
max(rivers)
```

    ## [1] 3710

``` r
min(rivers)
```

    ## [1] 135

##### (f) Make a list of all (lengths of) rivers longer than 1000 miles.

Solution:

``` r
x <- rivers[rivers > 1000]
x
```

    ##  [1] 1459 1450 1243 2348 1171 3710 2315 2533 1306 1054 1270 1885 1100 1205 1038
    ## [16] 1770

### 1.8 Consider the built-in data frame `airquality`.

##### (a) How many observations of how many variables are there?

Answer: **153 observations, 6 variables**

Solution:

``` r
str(airquality)
```

    ## 'data.frame':    153 obs. of  6 variables:
    ##  $ Ozone  : int  41 36 12 18 NA 28 23 19 8 NA ...
    ##  $ Solar.R: int  190 118 149 313 NA NA 299 99 19 194 ...
    ##  $ Wind   : num  7.4 8 12.6 11.5 14.3 14.9 8.6 13.8 20.1 8.6 ...
    ##  $ Temp   : int  67 72 74 62 56 66 65 59 61 69 ...
    ##  $ Month  : int  5 5 5 5 5 5 5 5 5 5 ...
    ##  $ Day    : int  1 2 3 4 5 6 7 8 9 10 ...

##### (b) What are the names of the variables?

Answer: **Ozone, Solar.R, Wind, Temp, Month, Day**

### 1.8 Consider the built-in data frame `airquality`.

##### (c) What type of data is each variable?

Answer: **Ozone: int, Solar.R: int, Wind: num, Temp: int, Month: int,
Day: int**

##### (d) Do you agree with the data type that has been given to each variable? What would have been some alternative choices?

Answer: **Ozone, Solar.R, and Temp all could be represented by nums.
Specificity is lost using int. The int type are understandable
representations of the Month and Day variables since they represent
whole days and whole months.**

### 1.9 There is a built-in data set `state`, which is really seven separate variables with names such as `state.name`, `state.region`, and `state.area`.

##### (a) What are the possible regions a state can be in? How many states are in each region?

Answer: **Northeast: 9, South: 16, North Central: 12, West: 13**

Solution:

``` r
table(state.region)
```

    ## state.region
    ##     Northeast         South North Central          West 
    ##             9            16            12            13

##### (b) Which states have area less than 10,000 square miles?

Answer: **“Connecticut”, “Delaware”, “Hawaii”, “Massachusetts”, “New
Hampshire”, “New Jersey”, “Rhode Island”, “Vermont”**

Solution:

``` r
state.name[which(state.area < 10000)]
```

    ## [1] "Connecticut"   "Delaware"      "Hawaii"        "Massachusetts"
    ## [5] "New Hampshire" "New Jersey"    "Rhode Island"  "Vermont"

##### (c) Which state’s geographic center is furthest south? (Hint: use `which.min`)

Answer: **Alaska**

Solution:

``` r
df <- data.frame(state.center, row.names = state.name)
df[which.min(df$x),]
```

    ##              x     y
    ## Alaska -127.25 49.25

### 1.10 Consider the `mtcars` data set.

##### (a) Which cars have 4 forward gears?

Answer: **Mazda RX4, Mazda RX4 Wag, Datsun 710, Merc 240D, Merc 230,
Merc 280, Merc 280C, Fiat 128, Honda Civic, Toyota Corolla, Fiat X1-9,
Volvo 142E**

Solution:

``` r
mtcars[mtcars$gear == 4,]
```

    ##                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb
    ## Mazda RX4      21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
    ## Mazda RX4 Wag  21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
    ## Datsun 710     22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
    ## Merc 240D      24.4   4 146.7  62 3.69 3.190 20.00  1  0    4    2
    ## Merc 230       22.8   4 140.8  95 3.92 3.150 22.90  1  0    4    2
    ## Merc 280       19.2   6 167.6 123 3.92 3.440 18.30  1  0    4    4
    ## Merc 280C      17.8   6 167.6 123 3.92 3.440 18.90  1  0    4    4
    ## Fiat 128       32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
    ## Honda Civic    30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
    ## Toyota Corolla 33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
    ## Fiat X1-9      27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
    ## Volvo 142E     21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2

##### (b) What subset of `mtcars` does `mtcars[mtcars$disp > 150 & mtcars$mpg > 20,]` describe?

Answer: **Cars whose displacement is greater than 150 and miles per
gallon is greater than 20.**

Solution:

``` r
mtcars[mtcars$disp > 150 & mtcars$mpg > 20,]
```

    ##                 mpg cyl disp  hp drat    wt  qsec vs am gear carb
    ## Mazda RX4      21.0   6  160 110 3.90 2.620 16.46  0  1    4    4
    ## Mazda RX4 Wag  21.0   6  160 110 3.90 2.875 17.02  0  1    4    4
    ## Hornet 4 Drive 21.4   6  258 110 3.08 3.215 19.44  1  0    3    1

##### (c) Which cars have $4$ forward gears and manual transmission? (Note: manual transmission is $1$ and automatic is $0$.)

Answer: **Mazda RX4, Mazda RX4 Wag, Datsun 710, Fiat 128, Honda Civic,
Toyota Corolla, Fiat X1-9, Volvo 142E**

Solution:

``` r
mtcars[mtcars$gear == 4 & mtcars$am == 1,]
```

    ##                 mpg cyl  disp  hp drat    wt  qsec vs am gear carb
    ## Mazda RX4      21.0   6 160.0 110 3.90 2.620 16.46  0  1    4    4
    ## Mazda RX4 Wag  21.0   6 160.0 110 3.90 2.875 17.02  0  1    4    4
    ## Datsun 710     22.8   4 108.0  93 3.85 2.320 18.61  1  1    4    1
    ## Fiat 128       32.4   4  78.7  66 4.08 2.200 19.47  1  1    4    1
    ## Honda Civic    30.4   4  75.7  52 4.93 1.615 18.52  1  1    4    2
    ## Toyota Corolla 33.9   4  71.1  65 4.22 1.835 19.90  1  1    4    1
    ## Fiat X1-9      27.3   4  79.0  66 4.08 1.935 18.90  1  1    4    1
    ## Volvo 142E     21.4   4 121.0 109 4.11 2.780 18.60  1  1    4    2

##### (d) Which cars have 4 forward gears or manual transmission?

Answer: **“Mazda RX4” “Mazda RX4 Wag” “Datsun 710” “Merc 240D” “Merc
230” “Merc 280” “Merc 280C” “Fiat 128” “Honda Civic” “Toyota Corolla”
“Fiat X1-9” “Porsche 914-2” “Lotus Europa” “Ford Pantera L” “Ferrari
Dino” “Maserati Bora” “Volvo 142E”**

Solution:

``` r
rownames(mtcars)[which(mtcars$gear == 4 | mtcars$am == 1,)]
```

    ##  [1] "Mazda RX4"      "Mazda RX4 Wag"  "Datsun 710"     "Merc 240D"     
    ##  [5] "Merc 230"       "Merc 280"       "Merc 280C"      "Fiat 128"      
    ##  [9] "Honda Civic"    "Toyota Corolla" "Fiat X1-9"      "Porsche 914-2" 
    ## [13] "Lotus Europa"   "Ford Pantera L" "Ferrari Dino"   "Maserati Bora" 
    ## [17] "Volvo 142E"

##### (e) Find the mean mpg of the cars with 2 carburetors.

Answer: **22.4**

Solution:

``` r
mean(mtcars$mpg[which(mtcars$carb == 2)])
```

    ## [1] 22.4

### 1.11 Consider the `mtcars` data set.

##### (a) Convert the `am` variable to a factor with two levels, `auto` and `manual`, by typing the following: `mtcars$am <- factor(mtcars$am, levels = c(0, 1), labels = c("auto", "manual"))`.

Solution:

``` r
mtcars$am <- factor(mtcars$am, levels = c(0, 1), labels = c("auto", "manual"))
```

##### (b) How many cars of each type of transmission are there?

Answer: **auto: 19, manual: 13**

Solution:

``` r
mtcars$am <- factor(mtcars$am, levels = c(0, 1), labels = c("auto", "manual"))
table(mtcars$am)
```

    ## 
    ##   auto manual 
    ##      0      0

##### (c) How many cars of each type of transmission have gas mileage estimates greater than 25 mpg?

Answer: **auto: 0, manual: 6**

Solution:

``` r
table(mtcars$am[which(mtcars$mpg > 25)])
```

    ## 
    ##   auto manual 
    ##      0      0

### 1.12 This problem uses the data set `hot_dogs from the package`fosdata\`.

##### (a) How many observations of how many variables are there? What types are the variables?

Answer: **type(Beef): 20, type(Meat): 17, type(Poultry): 17,
calories:54, sodium: 54**

Solution:

``` r
library(fosdata)
str(hot_dogs)
```

    ## 'data.frame':    54 obs. of  3 variables:
    ##  $ type    : Factor w/ 3 levels "Beef","Meat",..: 1 1 1 1 1 1 1 1 1 1 ...
    ##  $ calories: int  186 181 176 149 184 190 158 139 175 148 ...
    ##  $ sodium  : int  495 477 425 322 482 587 370 322 479 375 ...

``` r
table(hot_dogs$type)
```

    ## 
    ##    Beef    Meat Poultry 
    ##      20      17      17

##### (b) What are the three kinds of hot dogs in this data set?

Answer: **type(Beef): 20, type(Meat): 17, type(Poultry)**

Solution:

``` r
library(fosdata)
table(hot_dogs$type)
```

    ## 
    ##    Beef    Meat Poultry 
    ##      20      17      17

##### (c) What is the highest sodium content of any hot dog in this data set?

Answer: **645**

Solution:

``` r
max(hot_dogs$sodium)
```

    ## [1] 645

##### (d) What is the mean calorie content for Beef hot dogs?

Answer: **156.85**

Solution:

``` r
mean(hot_dogs$calories[which(hot_dogs$type == "Beef")])
```

    ## [1] 156.85

### 1.13 This problem uses the data set `DrinksWages` from the package `HistData`.

##### (a) How many observations of how many variables are there? What types are the variables?

Answer: **70 observations; class, trade, sober, drinks, wage, n**

Solution:

``` r
library(HistData)
```

    ## Warning: package 'HistData' was built under R version 4.4.2

``` r
str(DrinksWages)
```

    ## 'data.frame':    70 obs. of  6 variables:
    ##  $ class : Factor w/ 3 levels "A","B","C": 1 1 1 1 1 1 1 1 1 1 ...
    ##  $ trade : Factor w/ 70 levels "baker","barman",..: 38 10 25 55 36 44 68 34 14 11 ...
    ##  $ sober : int  1 1 2 1 2 9 8 3 0 12 ...
    ##  $ drinks: int  1 10 1 5 0 8 2 5 7 23 ...
    ##  $ wage  : num  24 18.4 21.5 21.2 19 ...
    ##  $ n     : int  2 11 3 6 2 17 10 8 7 35 ...

##### (b) The variable `wage` contains the average wage for each profession. Which profession has the lowest wage?

Answer: **factory worker**

Solution:

``` r
library(HistData)
DrinksWages$trade[which.min(DrinksWages$wage)]
```

    ## [1] factory worker
    ## 70 Levels: baker barman billposter blacksmith bookbinder ... wireworker

##### (c) The variable `n` contains the number of workers surveyed for each profession. Sum this to find the total number of workers surveyed.

Answer: **604**

Solution:

``` r
library(HistData)
sum(DrinksWages$n)
```

    ## [1] 604

##### (d) Compute the mean wage for all workers surveyed by multiplying {} for each profession, summing, and dividing by the total number of workers surveyed.

Answer: **24.59782**

Solution:

``` r
library(HistData)
total_workers <- sum(DrinksWages$n)
total_wages <- sum(DrinksWages$wage * DrinksWages$n)
mean_wage <- total_wages / total_workers
mean_wage
```

    ## [1] 24.59782

### 1.14 This problem uses the package `Lahman`, which needs to be installed on your computer. The data set `Batting`, in the `Lahman` package contains batting statistics of all major league baseball players since 1871, broken down by season.

##### (a) How many observations of how many variables are there?

Answer: **113,799 observations of 22 variables**

Solution:

``` r
library("Lahman")
```

    ## Warning: package 'Lahman' was built under R version 4.4.2

``` r
str(Batting)
```

    ## 'data.frame':    113799 obs. of  22 variables:
    ##  $ playerID: chr  "aardsda01" "aardsda01" "aardsda01" "aardsda01" ...
    ##  $ yearID  : int  2004 2006 2007 2008 2009 2010 2012 2013 2015 1954 ...
    ##  $ stint   : int  1 1 1 1 1 1 1 1 1 1 ...
    ##  $ teamID  : Factor w/ 149 levels "ALT","ANA","ARI",..: 117 35 33 16 116 116 93 94 4 80 ...
    ##  $ lgID    : Factor w/ 7 levels "AA","AL","FL",..: 5 5 2 2 2 2 2 5 5 5 ...
    ##  $ G       : int  11 45 25 47 73 53 1 43 33 122 ...
    ##  $ AB      : int  0 2 0 1 0 0 0 0 1 468 ...
    ##  $ R       : int  0 0 0 0 0 0 0 0 0 58 ...
    ##  $ H       : int  0 0 0 0 0 0 0 0 0 131 ...
    ##  $ X2B     : int  0 0 0 0 0 0 0 0 0 27 ...
    ##  $ X3B     : int  0 0 0 0 0 0 0 0 0 6 ...
    ##  $ HR      : int  0 0 0 0 0 0 0 0 0 13 ...
    ##  $ RBI     : int  0 0 0 0 0 0 0 0 0 69 ...
    ##  $ SB      : int  0 0 0 0 0 0 0 0 0 2 ...
    ##  $ CS      : int  0 0 0 0 0 0 0 0 0 2 ...
    ##  $ BB      : int  0 0 0 0 0 0 0 0 0 28 ...
    ##  $ SO      : int  0 0 0 1 0 0 0 0 1 39 ...
    ##  $ IBB     : int  0 0 0 0 0 0 0 0 0 NA ...
    ##  $ HBP     : int  0 0 0 0 0 0 0 0 0 3 ...
    ##  $ SH      : int  0 1 0 0 0 0 0 0 0 6 ...
    ##  $ SF      : int  0 0 0 0 0 0 0 0 0 4 ...
    ##  $ GIDP    : int  0 0 0 0 0 0 0 0 0 13 ...

##### (b) Use the command `head(Batting)` to get a look at the first six lines of data.

Solution:

``` r
install.packages("Lahman")
```

    ## Warning: package 'Lahman' is in use and will not be installed

``` r
library("Lahman")
head(Batting)
```

    ##    playerID yearID stint teamID lgID  G AB R H X2B X3B HR RBI SB CS BB SO IBB
    ## 1 aardsda01   2004     1    SFN   NL 11  0 0 0   0   0  0   0  0  0  0  0   0
    ## 2 aardsda01   2006     1    CHN   NL 45  2 0 0   0   0  0   0  0  0  0  0   0
    ## 3 aardsda01   2007     1    CHA   AL 25  0 0 0   0   0  0   0  0  0  0  0   0
    ## 4 aardsda01   2008     1    BOS   AL 47  1 0 0   0   0  0   0  0  0  0  1   0
    ## 5 aardsda01   2009     1    SEA   AL 73  0 0 0   0   0  0   0  0  0  0  0   0
    ## 6 aardsda01   2010     1    SEA   AL 53  0 0 0   0   0  0   0  0  0  0  0   0
    ##   HBP SH SF GIDP
    ## 1   0  0  0    0
    ## 2   0  1  0    0
    ## 3   0  0  0    0
    ## 4   0  0  0    0
    ## 5   0  0  0    0
    ## 6   0  0  0    0

##### (c) What is the most number of triples (`X3B`) that have been hit in a single season?

Answer: **36**

Solution:

``` r
install.packages("Lahman")
```

    ## Warning: package 'Lahman' is in use and will not be installed

``` r
library("Lahman")
max(Batting$X3B)
```

    ## [1] 36

##### (d) What is the playerID(s) of the person(s) who hit the most number of triples in a single season? In what year did it happen?

Answer: **“wilsoch01”, 1912**

Solution:

``` r
install.packages("Lahman")
```

    ## Warning: package 'Lahman' is in use and will not be installed

``` r
library("Lahman")
Batting$playerID[which.max(Batting$X3B)]
```

    ## [1] "wilsoch01"

``` r
Batting$yearID[which.max(Batting$X3B)]
```

    ## [1] 1912

##### (e) Which player hit the most number of triples in a single season since 1960?

Answer: **“delanro01”**

Solution:

``` r
install.packages("Lahman")
```

    ## Warning: package 'Lahman' is in use and will not be installed

``` r
library("Lahman")
Batting$playerID[which.max(Batting$X3B[Batting$yearID >= 1960])]
```

    ## [1] "delanro01"

### 1.15 Consider the `bechdel` data set in the `fosdata` package.

##### (a) How many movies in the data set pass the Bechdel test?

Answer: **803**

Solution:

``` r
library("fosdata")
sum(bechdel$binary == "PASS")
```

    ## [1] 803

##### (b) What percentage of movies in the data set pass the Bechdel test?

Answer: **0.4476031**

Solution:

``` r
library("fosdata")
sum(bechdel$binary == "PASS") / nrow(bechdel)
```

    ## [1] 0.4476031

##### (c) Create a table of number of movies in the data set by year.

Answer: ** 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980 1981
1982 1983 1984 1985 1986 1987 1988 1989 1990 1991 1 5 3 5 7 5 8 7 8 5 14
9 14 5 16 10 10 14 19 14 15 13 1992 1993 1994 1995 1996 1997 1998 1999
2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 20
16 26 36 42 51 62 56 63 64 80 64 81 100 90 73 101 124 129 124 86 99 **

Solution:

``` r
library("fosdata")
table(bechdel$year)
```

    ## 
    ## 1970 1971 1972 1973 1974 1975 1976 1977 1978 1979 1980 1981 1982 1983 1984 1985 
    ##    1    5    3    5    7    5    8    7    8    5   14    9   14    5   16   10 
    ## 1986 1987 1988 1989 1990 1991 1992 1993 1994 1995 1996 1997 1998 1999 2000 2001 
    ##   10   14   19   14   15   13   20   16   26   36   42   51   62   56   63   64 
    ## 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 
    ##   80   64   81  100   90   73  101  124  129  124   86   99

##### (d) Which year has the most movies in the data set?

Answer: **2010 with 129 movies**

Solution:

``` r
library("fosdata")
table(bechdel$year)[which.max(table(bechdel$year))]
```

    ## 2010 
    ##  129

##### (e) How many different values are there in the `clean_test` variable?

Answer: **5 levels; “dubious”, “men”, “notalk”, “nowomen”, “ok”**

Solution:

``` r
library("fosdata")
str(bechdel$clean_test)
```

    ##  Factor w/ 5 levels "dubious","men",..: 3 5 3 3 2 2 3 5 5 3 ...

``` r
levels(bechdel$clean_test)
```

    ## [1] "dubious" "men"     "notalk"  "nowomen" "ok"

##### (f) Create a data frame that contains only those observations that pass the Bechdel test.

Solution:

``` r
library("fosdata")
pass_bechdel <- bechdel[which(bechdel$binary == "PASS"),]
```
