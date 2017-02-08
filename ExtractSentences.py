#Extract from DUC2002Test/summaries/dnnnxx/perdocs 
#Two documents contains two summaries for same document
#

#write to reference/task1_englishReserence1.txt and task1_englishReference2.txt
#Every sentence separate in one line.

#so when trying to write to files, make the file name according to the inputname
#fileName: filename_referenceN.txt
import os
import nltk

currentPath = os.path.abspath('.')
reference = 'DUC2002Test/summaries'
referencePath = os.path.join(currentPath, reference)
#i = 0
filename = ''
flag = 0
for folder in os.listdir(referencePath):
	#mac system contains .Dstore file
	#if folder.find('.')==-1:
		#print folder
	folderPath = os.path.join(referencePath, folder)
	summariesPath = os.path.join(folderPath, 'perdocs')
	if os.path.exists(summariesPath):
		with open(summariesPath) as f:
			lines= f.readlines()
			
			for x in xrange(0,len(lines)):

				lines[x] = lines[x].strip()
				line= lines[x]
				if line.find('DOCREF=')!=-1:
					#line = line.strip()
					filename = line[8:-1].strip()
					x = x+4
					n=1
					#referenceFilename = 'reference/'+filename+'_reference0.txt'
					#referenceFilename = 'reference/'+filename+'_reference0'
					referenceWithOutTxt = 'reference/'+filename+'_reference'
					#n = 1
					referenceFilename = referenceWithOutTxt+str(n)+'.txt'
					while os.path.exists(referenceFilename):
						n=n+1
						referenceFilename = referenceWithOutTxt+str(n)+'.txt'
						#referenceFilename = referenceFilename[0:-1]+str(n)
						#referenceFilename = referenceFilename+n
						

					# if os.path.exists(referenceFilename):
					# 	#if the file exists, showing that the reference have already exist 1 version
					# 	referenceFilename = 'reference/'+filename+'_reference2'+'.txt'
					# if os.path.exists(referenceFilename):
					# 	referenceFilename = 'reference/'+filename+'_reference3'+'.txt'
					
					sentence = []
					#lines[x] = lines[x].strip()
					while len(lines[x].strip())!=0:
						lines[x] = lines[x].strip()
						#write to file
						end = lines[x].find('</SUM>')
						if end!=-1:
							lines[x]= lines[x][0:end]
						sentence.append(lines[x])
							#print lines[x]
							#write to the correspanding file
						
							#f1.write(lines[x].strip())
						x+=1
						if x>=len(lines):
							break
					paragraph = ' '.join(sentence)
					sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
					sentenceTokens = sent_detector.tokenize(paragraph.strip())
					with open(referenceFilename, 'w') as f1:
						for y in xrange(0,len(sentenceTokens)):
							f1.write(sentenceTokens[y])
							if y!=len(sentenceTokens)-1:
								f1.write('\n')
							#f1.write('\n')
					flag = flag+1
					#print '====================='
				else:
					continue
print 'total Number: %d'%flag




			# for line in f.readlines():
			# 	#print line
			# 	if line.find('DOCREF=')!=-1:
					
			# 		#print 'line: %s'%line
			# 		line = line.strip()
			# 		filename = line[8:-1].strip()
			# 		#Write to file
			# 		#when the file is exist, name it with number suffix
			# 	if len(line.strip())==0:

			# 		pass