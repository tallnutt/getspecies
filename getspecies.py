
import sys
import re


#usage 
#C:\Python27>getotus1.py C:\Python27\POLLEN1195BDAILY\mid
#outputs tab delim file of counts of each top hit taxa from the blast input file 


mid_hits = sys.argv[1] #file path plus start of name up to file number, e.g. 'mid'
bit_score = int(sys.argv[2]) #bit score threshold e.g. 200
#exclude_num = sys.argv[3]

f2 = open("species_summary.txt",'a')
#get taxa names (genera only)
i1=0
i2=0
n1=0
score1=10.0
num_taxa=0
taxalist=[]
#loop through specified mids
midlist1 = [33]#1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,23,24,25,26, 27, 28, 29,30, 31, 32, 34]#, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 92, 93, 94, 96, 97]
for mid_num in midlist1:
	a=[]
	n1=0
	#open blast hit files
	with open(str(mid_hits) + str(mid_num) + "hits.txt") as f:
		#search lines for > and extract taxon name
		for line in f:
			
			if line[:1] == '>':
				n1 = n1+1
				text1=line[3:70]
				spaces1 = [n for n in xrange(len(text1)) if text1.find(' ', n) == n]
				i1 = spaces1[0] #1st space plus text1 string start position (4)
				i2 = spaces1[1]
				i3 = spaces1[2]
				x1 =line[i1+4:i3+3]
				
				a.append(x1)
				
			if line[:8] == ' Score =':
				score1 = float(line[9:14])
				
				if score1 < bit_score:
					n1=n1-1
					a.remove(x1)
						
	a.sort()
	b=[]
	count_tax=0
	#count elements of list and record to file
	a.append(" ")
	b.append(a[0]) #kickoff the count list with the first entry of taxa list
		
	#print a
	#print a[0]
	#print a[n1]
	#count taxa in main list
	count_tax=0
	for p1 in range(1,n1+1):
		#print count_tax+1
		#print exclude_num
		#raw_input()
		if a[p1-1] == a[p1]: 
			count_tax=count_tax + 1
		
		if a[p1-1] <> a[p1]:     # and count_tax+1 >= exclude_num:
			#raw_input()
			#print count_tax+1
			#print exclude_num
			#if count_tax+1 >= exclude_num:
			#print "yes"
			b.append(count_tax+1)
			b.append(a[p1])
			count_tax=0
		
	#print b #list of taxa and freqs
	f1 = open(mid_hits + str(mid_num) + "_species.txt",'a')
	print "MID_" + str(mid_num)
	for x2 in xrange(0, len(b)-1,2):
		print str(b[x2]) + "\t" + str(b[x2+1])
		f1.write(str(b[x2]) + "\t" + str(b[x2+1]) + "\n")
	
	#add taxa to master list
	for x3 in xrange(0, len(b)-1,2):
		
		if taxalist.count(b[x3])==0:#if a taxon not present in list
			num_taxa = num_taxa+1
			taxalist.append(b[x3]) #add new taxa if not found in list
	
		
	taxalist.sort()
	print taxalist
	f1.close()
	print "==============================================="
#print taxalist
#final loop = mid number cycle
for item1 in taxalist:
	f2.write(item1 + '\t')


f2.close()
	
	