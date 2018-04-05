import threading as th
import time

	def report_memory_consumption():
	# go through `gc.get_objects()`, check their size and print a summary
	# takes ~5 min to run

	def memory_daemon():
	  while True:
	    # all other threads should not do anything until this call is complete
	    report_memory_consumption()
	    # sleep for 10 sec, then update memory summary
	    # this sleep is the only time when other threads should be executed
	    time.sleep(10)


	def f1():
	  # do something, including calling many other functions
	  # takes ~3 min to run
		print('f1')

	def f2():
	  # do something, including calling many other functions
	  # takes ~3 min to run
		print('f2')

def main():
  t_mem = th.Thread(target = memory_daemon)
  t1 = th.Thread(target = f1)
  t2 = th.Thread(target = f2)
  t_mem.start()
  t1.start()
  t2.start()
