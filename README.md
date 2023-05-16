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

 Picking a new state within partition:

| value | meaning 
| ---   |  ---
| 3     | Memoryfull (state unchanged)
| 2     | Uniformly random state
| 1     | Upper bound
| 0     | Middle
| -1    | Lower bound
| -2    | Least energy preserved for bouncing ball
| -3    | Most energy preserved for bouncing ball

Observed reward:

| value | meaning
| ---   | ---
| 2     | Sample (actual cost)
| 1     | Upper bound
| 0     | Middle
| -1    | Lower bound