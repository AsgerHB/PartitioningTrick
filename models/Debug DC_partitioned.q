//This file was generated from (Academic) UPPAAL 4.1.20-stratego-11 (rev. 323D987339A98B21), December 2022

/*

*/
//NO_QUERY

/*
--print-strategies=strats --discount 0.9 --good-runs 1000 --total-runs 1000 --runs-pr-state 1000 --max-iterations 10 --reset-no-better 10 --random-search-limit 0.5 --deterministic-search-limit 0.8 --split-filter-rate 1 --split-ks 0.2 --split-lower-t 0.05 --split-upper-t 1.8 --learning-method 5 -D0.5
*/
strategy S = minE(dist) [<=1000] {Converter.location} -> {x1, x2}: <> time >= 1000

/*

*/
strategy S2 = minE(dist) [<=1000] {Converter.location} -> {iI, iV}: <> time >= 1000

/*

*/
simulate [<=120;20] {x1,x2, 7 + Converter.d1u1, 9 + Converter.d1u0, 11 + Converter.d0u0, fabs(x2-x2ref), 14.8,  15.2 , 0.7} under S

/*

*/
simulate [<=120;1] {x1, Il,Iu, x2, Vl, Vu, V_min,  V_max, I_max}

/*

*/
simulate [<=120;1] {x1, Il,Iu, x2, Vl, Vu, V_min,  V_max, I_max} under S

/*

*/
simulate [<=120;1] {x1, Il,Iu, x2, Vl, Vu, V_min,  V_max, I_max} under S2

/*

*/
simulate [<=120;1] {x_R, Rl, Ru, R_min, R_max}

/*

*/
simulate [<=120;10] {x1, x2, 14.5,  15.5 , 4} under S3

/*

*/
E[<=120;100] (max: switches) under S

/*

*/
E[<=120;100] (max: switches) under S2

/*

*/
E[<=120;100] (max: switches) under S3

/*

*/
E[<=120;100] (max: number_deaths)

/*

*/
E[<=120;100] (max: number_deaths) under S

/*

*/
E[<=120;100] (max: number_deaths) under S2

/*

*/
E[<=120;100] (max: number_deaths) under S3

/*

*/
E[<=120;100] (max: dist)

/*

*/
E[<=120;100] (max: dist) under S

/*

*/
E[<=120;100] (max: dist) under S2

/*

*/
E[<=120;100] (max: dist) under S3

/*

*/
simulate [<=120;2] {x_R}

/*

*/
Pr[<=50;10000] (<> number_deaths > 0 )

/*

*/
Pr[<=50;10000] (<> number_deaths > 0 ) under S

/*

*/
Pr[<=50;10000] (<> number_deaths > 0 ) under S2

/*

*/
saveStrategy("Results/Misc/DC.strategy.json", S)

/*

*/
strategy S = loadStrategy {Converter.location} -> {x1, x2} ("/home/asger/Results/fig-DCShieldingResultsGroup/Query Results/0/NoShield/12000Runs/Deterrence0.strategy.json")
