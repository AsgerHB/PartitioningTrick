# Q-PART

Strategies can be viewed with "x StrategyVisualisation.jl" for x ∈ {RW} using [Pluto Notebooks](https://github.com/fonsp/Pluto.jl) 

 - [x] Partitioned BB
 - [ ] BB strategy visualisation (I have some copy-pasta from this)
 - [x] Partitioned RW
 - [x] RW strategy visualisation
 - [?] Partitioned DC
 - [ ] 1D example
 - [ ] 2D example
 - [ ] More versatile plotting code

 ## Magic Numbers

 Picking a new state within partition: (`Ax` parameters)

| value | meaning 
| ---   |  ---
| 3     | Memoryfull (state unchanged)
| 2     | Uniformly random state
| 1     | Upper bound
| 0     | Middle
| -1    | Lower bound
| -2    | Least energy preserved for bouncing ball
| -3    | Most energy preserved for bouncing ball

Observed reward: (`C` parameter)

| value | meaning
| ---   | ---
| 2     | Sampled
| 1     | Best partition cost
| 0     | Average partition cost
| -1    | Worst partition cost