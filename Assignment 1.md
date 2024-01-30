<a name="br1"></a> 

Artiﬁcial Intelligence – Programming Assignment 1

Handed out:

Due:

10-Oct-2023

29-Oct-2023

In this lab assignment you will help Pacman ﬁnd paths through his maze world in order

to reach a particular location as well as to collect food eﬃciently. You will implement

general search algorithms and model their heuristics, applying them to scenarios from the

Pacman universe.

The code that describes the behavior of Pacman’s universe is already functional, while

you simply need to implement the algorithms which will control the way Pacman moves.

The code for the project consists of Python ﬁles, a part of which you just need to read

and understand, a part of which you need to modify yourselves and a part that you can

ignore. After you download and unpack the zip archive, you will see a list of ﬁles and

folders which we brieﬂy describe below:

Files you’ll edit:

search.py

searchAgents.py

Files you should look at:

Where all of your search algorithms are

Where all of your search-based agents are

pacman.py

game.py

util.py

The main ﬁle that runs Pacman games

The logic behind how the Pacman world works

Useful data structures for implementing search algorithms

Supporting ﬁles you can ignore:

graphicsDisplay.py

graphicsUtils.py

textDisplay.py

ghostAgents.py

keyboardAgents.py

autograder.py

testParser.py

Graphics for Pacman

Support for Pacman graphics

ASCII graphics for Pacman

Agents to control ghosts

Keyboard interfaces to control Pacman

Project autograder (Berkeley)

Parses autograder test and solution ﬁles (Berkeley)

General autograding test classes (Berkeley)

Directory containing the test cases for each question

testClasses.py

test cases/

searchTestClasses.py Project 1 speciﬁc autograding test classes (Berkeley)

The code for the lab assignments was adapted from the course ”Intro to AI” at Berkeley,

which allowed the usage of their Pacman environment for other universities for educational

purposes. The code is written in Python 2.7, which you require an interpreter for in order

to run the lab assignment.

1



<a name="br2"></a> 

Artiﬁcial Intelligence – Programming Assignment 1

After you’ve downloaded and unpacked the code and positioned your console in the

subdirectory where you have unpacked the archive, you can test the game by typing:

python pacman.py

However, artiﬁcial intelligence cannot rely on human control - Pacman has to be able to

independently and eﬃciently ﬁght all problems he might encounter on the way to ﬁnding

food! A naive example of artiﬁcial intelligence is always moving in the same direction

regardless of the map layout, which you can check by running the following:

python pacman.py --layout testMaze --pacman GoWestAgent

In this case, we passed the map testMaze and the logic that moves pacman west

GoWestAgent as arguments to the game. As you can assume yourselves, this approach

might hit a few roadbumps on the way when there is any turning required to reach the

goal, as is evident from the following example:

python pacman.py --layout tinyMaze --pacman GoWestAgent

Through this lab assignment you will allow Pacman not only to navigate through the

previous two mazes, but through any other he might face. The pacman game has a lot of

possible arguments, and we recommend you study them yourselves by typing:

python pacman.py -h

All the commands you need to execute throughout the instructions for this lab assign-

ment will be present in the text ﬁle commands.txt. In case you are running a UNIX-based

system, you can run all the commands sequentially by typing bash commands.txt in your

console.

2



<a name="br3"></a> 

Artiﬁcial Intelligence – Programming Assignment 1

Problem 1: Finding food by depth ﬁrst search

In the ﬁle searchAgents.py you will ﬁnd a fully functional search agent (class SearchAgent),

which ﬁrst plans out the route through Pacman’s world, and then goes through the route

step by step. Your job is to implement the search algorithms which formulate the plans.

Firstly, check if the search agent is working as intended by running the following command:

python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch

The command passes the search algorithm tinyMazeSearch to the search agent. The

search algorithm is implemented in search.py, and by examining the code you will conclude

that it works only in the case of the map that we provided - now it is the time to write

the code which will ﬁnd the solution for any map layout.

The pseudocode for the search algorithms can be found in the lecture slides - keep in

mind that you don’t just need to ﬁnd the path to the goal state, but you also need to be

able to reproduce the steps once you’ve found it. The search node needs to contain not

only the information of the current state, but also the steps required to reach the state.

You should also use a data structure to keep track of all the visited states in order to

ensure completeness of the DFS algorithm.

Note 1.: All of your methods need to return a list of valid actions that will lead the

agent from the start to the goal. Validity in this case means that in no case should Pacman

walk through walls.

Note 2.: Make sure to use classes Stack, Queue and PriorityQueue classes in your

implementation, since the automatic testing relies on them, and that way you can validate

your solution easier.

Hint 1.: The lab assignment can be solved by simply ﬁlling out all the marked meth-

ods in the code - howevery by solving in that fashion you will encounter a lot of code

duplication. Since DFS, BFS, UCS and A\* diﬀer only in the selection of the next node

to be expanded, try to implement a single generic search method which can be conﬁgured

with an algorithm-speciﬁc queueing strategy. Your implementation does not need to be

in this form to get full points in the assignment.

Implement the depth-ﬁrst search (DFS) algorithm in the depthFirstSearch method in

the ﬁle search.py. Your implementation should clear the following mazes without any

issues:

python pacman.py -l tinyMaze -p SearchAgent

python pacman.py -l mediumMaze -p SearchAgent

python pacman.py -l bigMaze -z .5 -p SearchAgent

Pacman’s maze will color the explored states red, with brighter red meaning earlier

exploration. Is the order of exploration what you would have expected? Does pacman go

through all the explored states on the way to the goal? Can the number of explored states

in your solution vary, and if it can, what does the number of explored states depend on?

A sample of solving the bigMaze with DFS can be found at Figure 1.

3



<a name="br4"></a> 

Artiﬁcial Intelligence – Programming Assignment 1

Figure 1: An example of depth ﬁrst search

Problem 2: Breadth First Search

Implement the breadth-ﬁrst search (BFS) algorithm in the breadthFirstSearch method in

the ﬁle search.py. Again, keep track of visited states so you wouldn’t explore them again.

Test your code in the same way you did for depth-ﬁrst search:

python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

Does BFS ﬁnd a minimum cost solution? If not, you might have a bug in your code.

If pacman moves too slow for your taste, Pacman’s alter ego PacFlash is here - to make

Pacman show his true face, enable the option –frameTime 0 like in the following example:

python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5 --frameTime 0

In case you’ve written the code generically, your search code should work equally well

when applied to the eight-puzzle:

python eightpuzzle.py

Problem 3: Uniform Cost Search

While BFS will ﬁnd a path to the goal which requires the fewest actions, sometimes we

want to ﬁnd paths that are the best in some other sense - examples of this are medium-

DottedMaze and mediumScaryMaze.

4



<a name="br5"></a> 

Artiﬁcial Intelligence – Programming Assignment 1

The toll of the fear from going through ghost infested areas is surely greater than calm

and peaceful areas, as well as areas rich in food are deﬁnitely easier on the spirit than the

cold, dark and damp walls of the maze - and as such, every reasonable Pacman adapts his

route accordingly.

Implement the uniform-cost search algorithm in the method uniformCostSearch in

search.py. You should easily clear each of the three following examples, which diﬀer only

by the pre-deﬁned cost functions.

python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs

python pacman.py -l mediumDottedMaze -p StayEastSearchAgent

python pacman.py -l mediumScaryMaze -p StayWestSearchAgent

You should get very low and very high path costs for the last two examples respectively

due to their exponential cost functions. If you want to know more, you can ﬁnd the code

in searchAgents.py.

Problem 4: A\* search

Implement the A\* search algorithm in the aStarSearch method in the ﬁle search.py. A\*

takes a heuristic function as an argument, while a heuristic function accepts two arguments

\- the state in the search problem (the main argument) and the problem itself (for reference

information). The nullHeuristic in the ﬁle search.py is a trivial example.

You can test your A\* implementation on the original problem of ﬁnding a path through

a maze to a ﬁxed position using the Manhattan distance heuristic - implemented already

for you as manhattanheuristic in searchAgents.py.

python pacman.py -l bigMaze -z .5 -p SearchAgent

-a fn=astar,heuristic=manhattanHeuristic

(Write the command in a single line)

The solution using A\* search should be marginally faster than uniform-cost search -

our implementation of A\* solves the maze with 549 nodes expanded, while UCS expands

620\. The numbers may vary depending on ties in priority. Test your implementation on

the openMaze problem - what diﬀers compared to other search strategies?

5

