import os
from lxml import etree

currentPath = os.path.abspath('.')
document = 'docs.with.sentence.breaks'
docPath = os.path.join(currentPath, document)
#i = 0
#filename = ''
flag = 0
dest = 'FinalDocs'
for folder in os.listdir(docPath):
	#mac system contains .Dstore file
	#if folder.find('.')==-1:
		#print folder
	filePath = os.path.join(docPath, folder)
	if not os.path.isdir(filePath):
		continue
	for file in os.listdir(filePath):
		#file contains the name of the article
		fileName = os.path.join(filePath, file)
		#Using OSX, always contains file named '.DS_Store'
		if file.find('DS_Store')!=-1:
			continue
		if os.path.exists(fileName):
			#print fileName
			# extract all the sentences in the articles
			#some files contains '&', can not parsed directly
			#so read file to a string then use xpath
			with open(fileName) as f:
				whole= f.read()
			#print 'parsing %s'%filePath + '/ ' + fileName
			html = etree.HTML(whole)
			result = html.xpath('//text//s')

			
			#html = etree.parse(fileName)
			#result = html.xpath('//TEXT/s')
			#print result
			#print len(result)
			#destFileName = folder+'.'+file.strip()[0:-2]
			#since if the fileName are the same, the content are all the same
			#so just ignore the repeated files
			#totally 533 unique files
			#so finally I can go to summary them using the new algorithm
			destFileName = file.strip()[0:-2]
			finalFile = os.path.join(dest, destFileName)
			if os.path.exists(finalFile):
				repeatedFileName = filePath +'/  '+ destFileName
				print 'REPEATED : %s'%repeatedFileName
			with open(finalFile,'w') as f:
				for x in xrange(0,len(result)):
					f.write(result[x].text)
			flag = flag +1

					#print result[x].text
			pass
		pass
print 'Totally %d articles written'%flag
	# dxxxnPath = 
	# folderPath = os.path.join(docPath, folder)
	# summariesPath = os.path.join(folderPath, 'perdocs')
	# if os.path.exists(summariesPath):
	# 	with open(summariesPath) as f:
	# 		lines= f.readlines()