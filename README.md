# OS Semaphore Lab
 In this lab you will use the Python threading module to create producer and consumer threads as well as create mutex locks and semaphores to solve the Producer Consumer Buffer problem. You can find the example of this in the book: section 7.1.1, Figure 7.1, Figure 7.2.
 Here is the Python Thread module doc: https://docs.python.org/3/library/threading.html
 
 ## Set Up
 <ol>
 	<li>Create new anaconda environment using these commands</li>
 	<ul>
 		<li>conda create --name semaphore_lab python=3.13.1</li>
 		<li>conda activate semaphore_lab</li>
 	</ul>
 	<li>Pull starter code from GitHub Classroom</li>
 	<li>Open in VS code and switch to the semaphore_lab anaconda environment</li>
 	<li>When the lab is complete, push code to GitHub Classroom</li>
 </ol>
 
 ## Notes
 You will need to use the threading, time, and random modules to complete this lab. 
 
 ## Instructions
 <ol>
    <li><b>Buffer class</li></b></li>
     <ol>
       <li>The buffer class will represent the bounded buffer</li>
       <li>__init__ should take in size as a parameter</li>
       <li><b>Attributes</b></li>
         <ol>
           <li>size: size of the buffer</li>
           <li>items: list to store items in the buffer.</li>
           <li>in_pointer: initialize to 0</li>
           <li>out_pointer: initialize to 0</li>
 		<li>mutex: a threading lock</li>
 		<li>empty_slots: a threading semaphore to indicate how many slots are empty</li>
 		<li>full_slots: a threading semaphore to indicate how many slots are full</li>
 	</ol>
     </ol>
 	<br>
 <li><b>Producer class</b></li>
 The producer will produce items represented as integers to add to the buffer. This will subclass the threading Python class.
 	<ol>
       <li><b>Attributes</b></li>
         <ol>
           <li>buffer (required)</li>
 	<li>id (required): an int used to identify a producing process</li>
         </ol>
     <li><b>Methods</b></li>
       <ol>
         <li>produce(): Takes an item as a parameter and add the item to the buffer. It must acquire and relase appropriate locks. When the item is added to the buffer, print out "Produced: {item} at postition {position in the buffer}</li>
 	<li>run(): Overload the built in threading run() method to generate 10 random integers between 1 and 100 and produce to the buffer. Also print out "Producer {id} producting {item}..." after generating the item to add to the buffer. After producing, put the process to "sleep" for a random amount of time between 0.1 and 0.5. This simulates the time it takes to produce an item. </li>
 	<li>When updating the buffer pointers use this calculation: ({pointer} + 1) % {buffer size}</li>
       </ol>
     </ol>
       <br>
 <li><strong>Consumer Class</strong></li>
 The consumer class will consume items from the buffer. This will subclass the threading Python class.
 <ol>
 	<li><b>Attributes</b></li>
         <ol>
 		<li>buffer (required)</li>
 		<li>id (required): an int used to identify a producing process</li>
         </ol>
       <li><b>Methods</b></li>
         <ol>
           <li>consume: Consumes and returns an item from the buffer. It must acquire the appropriate locks. When the item is consumed, print "Consumed: {item} from position {position} </li>
 	<li>run(): Overload the built in threading run() method to consume 10 items from the buffer. Also print out "Consumer {id} consumed {item}..." after consuming. After consuming, put the process to "sleep" for a random amount of time between 0.1 and 0.5. This simulates the time it takes to consume an item. </li>
         </ol>
 </ol>
 <br>
 <li><strong>main</strong></li>
 In main create the following objects and threads:
 <ol>
 	<li>A buffer with size 5</li>
 	<li>Two producers</li>
 	<li>Two consumers</li>
 	<li>Start the producers and consumers</li>
 	<li>Join the producers and consumers</li>
 	<li>Once complete print "All producers and consumers have finished.</li>
 </ol>