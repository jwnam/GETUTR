# this module defines functions for importing annotation sets.
# these functions may contain information for the reading of
# specific datasets, including directory paths.


import utilityModule, os

# the test lambda takes one Gene instance as an argument
def getRefFlatUniq(genomeName, test = lambda g: True):
    genomeToFile=dict()
    geneAnnobyChrom = getRefFlatbyChrom(genomeName)
    geneAnno=dict()
    chromosomes=geneAnnobyChrom.keys()
    if genomeName=='hg19': 
    		chromosomes=[]
		for i in range(1,23)+['M', 'X', 'Y']: chromosomes.append('chr' + str(i))
    if genomeName=='danRer7':
    		chromosomes=[]
		for i in range(1,26)+['M']: chromosomes.append('chr' + str(i))
    if genomeName=='mm9':
    		chromosomes=[]
		for i in range(1,20)+['M', 'X', 'Y']: chromosomes.append('chr' + str(i))
    for chrom in chromosomes:
        genes = geneAnnobyChrom.get(chrom,[])
        for gene in genes: geneAnno[gene[2].name()]=gene[2]
    geneAnno2=dict()
    for genename in geneAnno.keys():
	geneAnno2[geneAnno[genename].geneID()]=geneAnno[genename]
    return geneAnno2

def getRefFlatbyChromUniq(genomeName, test = lambda g: True):
    genomeToFile=dict()
    geneAnnobyChrom = getRefFlatbyChrom(genomeName)
    geneAnno=dict(); geneAnnoChrom=dict()
    chromosomes=[]
    chromosomes=geneAnnobyChrom.keys()
    if genomeName=='hg19': 
    		chromosomes=[]
		for i in range(1,23)+['M', 'X', 'Y']: chromosomes.append('chr' + str(i))
    if genomeName=='danRer7':
    		chromosomes=[]
		for i in range(1,26)+['M']: chromosomes.append('chr' + str(i))
    if genomeName=='mm9':
    		chromosomes=[]
		for i in range(1,20)+['M', 'X', 'Y']: chromosomes.append('chr' + str(i))
    #if genomeName=='dm3':
    #		chromosomes =['chr2L', 'chr2R', 'chr3L', 'chr3R' ,'chr4', 'chrM', 'chrU', 'chrX'] #, 'chr2LHet', 'chr2RHet', 'chr3LHet', 'chr3RHet', 'chrUextra', 'chrXHet', 'chrYHet']	
    for chrom in chromosomes: geneAnnoChrom[chrom]=[]
    for chrom in chromosomes:
        genes = geneAnnobyChrom.get(chrom,[])
        for gene in genes: geneAnno[gene[2].name()]=gene[2]
    for genename in geneAnno.keys():
	geneAnnoChrom[geneAnno[geneID].chr()].append(geneAnno[genename])
    return geneAnnoChrom

def getNewRefFlatUniq(genomeName, method, tpSeqSample, test = lambda g: True):
    genomeToFile=dict()
    geneAnnobyChrom = getNewRefFlatbyChrom(genomeName, method, tpSeqSample)
    geneAnno=dict()
    chromosomes=[]
    chromosomes=geneAnnobyChrom.keys()
    if genomeName=='hg19': 
    		chromosomes=[]
		for i in range(1,23)+['M', 'X', 'Y']: chromosomes.append('chr' + str(i))
    if genomeName=='danRer7':
    		chromosomes=[]
		for i in range(1,26)+['M']: chromosomes.append('chr' + str(i))
    if genomeName=='mm9':
    		chromosomes=[]
		for i in range(1,20)+['M', 'X', 'Y']: chromosomes.append('chr' + str(i))
    #if genomeName=='dm3':
    #		chromosomes =['chr2L', 'chr2R', 'chr3L', 'chr3R' ,'chr4', 'chrM', 'chrU', 'chrX'] #, 'chr2LHet', 'chr2RHet', 'chr3LHet', 'chr3RHet', 'chrUextra', 'chrXHet', 'chrYHet']	
    #for i in range(1,23)+['M', 'X', 'Y']: chromosomes.append('chr' + str(i))
    for chrom in chromosomes:
        genes = geneAnnobyChrom.get(chrom,[])
        for gene in genes: geneAnno[gene[2].name()]=gene[2]
    geneAnno2=dict()
    for gene in geneAnno.values(): geneAnno2[gene.geneID()]=gene
    return geneAnno2  

def getNewRefFlatbyChromUniq(genomeName, method, tpSeqSample, test = lambda g: True):
    genomeToFile=dict()
    geneAnnobyChrom = getNewRefFlatbyChrom(genomeName, method, tpSeqSample)
    geneAnno=dict(); geneAnnoChrom=dict()
    chromosomes=[]
    chromosomes=geneAnnobyChrom.keys()
    if genomeName=='hg19': 
    		chromosomes=[]
		for i in range(1,23)+['M', 'X', 'Y']: chromosomes.append('chr' + str(i))
    if genomeName=='danRer7':
    		chromosomes=[]
		for i in range(1,26)+['M']: chromosomes.append('chr' + str(i))
    if genomeName=='mm9':
    		chromosomes=[]
		for i in range(1,20)+['M', 'X', 'Y']: chromosomes.append('chr' + str(i))
    #if genomeName=='dm3':
    #		chromosomes =['chr2L', 'chr2R', 'chr3L', 'chr3R' ,'chr4', 'chrM', 'chrU', 'chrX'] #, 'chr2LHet', 'chr2RHet', 'chr3LHet', 'chr3RHet', 'chrUextra', 'chrXHet', 'chrYHet']	
    #for i in range(1,23)+['M', 'X', 'Y']: chromosomes.append('chr' + str(i))
    for chrom in chromosomes:
        genes = geneAnnobyChrom.get(chrom,[])
        for gene in genes: geneAnno[gene[2].name()]=gene[2]
    for chrom in chromosomes: geneAnnoChrom[chrom]=[]
    for genename in geneAnno.keys():
	geneAnnoChrom[geneAnno[geneID].chr()].append(geneAnno[genename])
    return geneAnnoChrom

def getRefFlat(genomeName, key='symbol', test = lambda g: True):
    genomeToFile=dict()
    genomeToFile['ce6'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/refFlat.txt'
    genomeToFile['hg18_distinct'] = '/lab/bartel3_ata/jwnam/h.sapiens/nature_refSeq_distinct.fa'
    genomeToFile['hg19'] = '/lab/bartel3_ata/jwnam/h.sapiens/hg19/refFlat.txt'
    genomeToFile['GRCh37.66'] = '/lab/bartel3_ata/jwnam/h.sapiens/hg19/GRCh37.66.genePred2'
    genomeToFile['danRer6'] = '/lab/bartel3_ata/jwnam/zebrafish/refFlat.txt'
    genomeToFile['danRer7'] = '/lab/bartel3_ata/jwnam/zebrafish/danRer7/refFlat.txt'
    genomeToFile['mm9'] = '/lab/bartel6_ata/nam/mouse/annotation/refFlat_mm9.txt'
    genomeToFile['dm3'] = '/lab/bartel3_ata/jwnam/d.melanogaster/annotation/refFlat.txt'
    genomeToFile['sangerRna'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerRnaGene.txt'
    genomeToFile['sangerPseudogene'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerPseudoGene.txt'
    genomeToFile['sangerGene'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerGene.txt'
    genomeToFile['denovo_annotation']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/combined_step3.txt'
    genomeToFile['denovo_annotation_v1.3']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/combined_step3_v1.3.txt'
    genomeToFile['combined']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/newTest3P_directCombined.txt'
    genomeToFile['modEncode_Aggregate']='/lab/bartel1_ata/jwnam/Project/Celegans/modEncode/Robert_Aggregate/Aggregate_1003.integrated_transcripts.ucsc_browser.ws190.txt'
    filename = genomeToFile[genomeName]
    geneList = dict()
    f = open(filename)
   
    ##for human
    #chrD=dict()
    #for i in xrange(1,23): chrD['chr' + str(i)]=1
    #chrD['chrX']=1; chrD['chrY']=1; chrD['chrM']=1

    for line in f.readlines():
        raw_line = line.split('\t')
	if len(raw_line)==10: raw_line.insert(1, raw_line[0])
        name = raw_line[0]
 	geneID = raw_line[1]
        chr = raw_line[2]
        sense = raw_line[3]
        txCoords = map(int,raw_line[4:6])
        cdCoords = map(int,raw_line[6:8])
        exStarts = map(int,raw_line[9].split(',')[:-1])
        exEnds = map(int,raw_line[10].split(',')[:-1])
        # fix the edges to work with the Gene specs
        #exEnds = map(lambda n: n-1, exEnds)
        txCoords = [txCoords[0], txCoords[1] ]
        cdCoords = [cdCoords[0], max([cdCoords[1], 0])]
        if cdCoords[0]!=0 or cdCoords[1]!=0:
            newGene = utilityModule.Gene(name, geneID,chr,sense,txCoords,cdCoords,exStarts,exEnds)
            if key=='geneID': 
		if not(geneList.has_key(geneID)): geneList[geneID] = newGene
            else: 
		if not(geneList.has_key(geneID)): geneList[name] = newGene
    f.close()
    return geneList

def getRefFlat2(filename,test = lambda g: True):
    genomeToFile=dict()
    genomeToFile['ce6'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/refFlat.txt'
    genomeToFile['mm9'] = '/lab/bartel6_ata/nam/mouse/annotation/refFlat_mm9.txt'
    genomeToFile['dm3'] = '/lab/bartel3_ata/jwnam/d.melanogaster/annotation/refFlat.txt'
    genomeToFile['danRer6'] = '/lab/bartel3_ata/jwnam/zebrafish/refFlat.txt'
    genomeToFile['danRer7'] = '/lab/bartel3_ata/jwnam/zebrafish/danRer7/refFlat.txt'
    genomeToFile['hg18_distinct'] = '/lab/bartel3_ata/jwnam/h.sapiens/nature_refSeq_distinct.fa'
    genomeToFile['hg19'] = '/lab/bartel3_ata/jwnam/h.sapiens/hg19/refFlat.txt'
    genomeToFile['GRCh37.66'] = '/lab/bartel3_ata/jwnam/h.sapiens/hg19/GRCh37.66.genePred2'
    genomeToFile['sangerRna'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerRnaGene.txt'
    genomeToFile['sangerPseudogene'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerPseudoGene.txt'
    genomeToFile['sangerGene'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerGene.txt'
    genomeToFile['denovo_annotation']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/combined_step3.txt'
    genomeToFile['denovo_annotation_v1.3']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/combined_step3_v1.3.txt'
    genomeToFile['combined']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/newTest3P_directCombined.txt'
    genomeToFile['modEncode_Aggregate']='/lab/bartel1_ata/jwnam/Project/Celegans/modEncode/Robert_Aggregate/Aggregate_1003.integrated_transcripts.ucsc_browser.ws190.txt'
    geneList = dict()
    f = open(filename)
    for line in f.readlines():
        raw_line = line.split('\t')
        if len(raw_line)==10: raw_line.insert(1, raw_line[0])
        name = raw_line[0]
        geneID = raw_line[1]
        chr = raw_line[2]
        sense = raw_line[3]
        txCoords = map(int,raw_line[4:6])
        cdCoords = map(int,raw_line[6:8])
        exStarts = map(int,raw_line[9].split(',')[:-1])
        exEnds = map(int,raw_line[10].split(',')[:-1])
        # fix the edges to work with the Gene specs
        #exEnds = map(lambda n: n-1, exEnds)
        txCoords = [txCoords[0], txCoords[1] ]
        cdCoords = [cdCoords[0], max([cdCoords[1] ,0])]
        if cdCoords[0]!=0 or cdCoords[1]!=0:
            newGene = utilityModule.Gene(name, geneID,chr,sense,txCoords,cdCoords,exStarts,exEnds)
            if not(geneList.has_key(geneID)): geneList[geneID] = newGene
    f.close()
    return geneList

def getRefFlatbyChrom(genomeName,test = lambda g: True):
    genomeToFile=dict()
    genomeToFile['hg18'] = '/lab/bartel3_ata/jwnam/h.sapiens/refFlat.txt'
    genomeToFile['hg19'] = '/lab/bartel3_ata/jwnam/h.sapiens/hg19/refFlat.txt'
    genomeToFile['GRCh37.66'] = '/lab/bartel3_ata/jwnam/h.sapiens/hg19/GRCh37.66.genePred2'
    genomeToFile['ce6'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/refFlat.txt'
    genomeToFile['dm3'] = '/lab/bartel3_ata/jwnam/d.melanogaster/annotation/refFlat.txt'
    genomeToFile['mm9'] = '/lab/bartel6_ata/nam/mouse/annotation/refFlat_mm9.txt'
    genomeToFile['danRer6'] = '/lab/bartel3_ata/jwnam/zebrafish/refFlat.txt'
    genomeToFile['danRer7'] = '/lab/bartel3_ata/jwnam/zebrafish/danRer7/refFlat.txt'
    genomeToFile['sangerRna'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerRnaGene.txt'
    genomeToFile['sangerPseudogene'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerPseudoGene.txt'
    genomeToFile['sangerGene'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerGene.txt'
    genomeToFile['denovo_annotation']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/combined_step3.txt'
    genomeToFile['denovo_annotation_v1.3']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/combined_step3_v1.3.txt'
    genomeToFile['combined']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/newTest3P_directCombined.txt'
    genomeToFile['modEncode_Aggregate']='/lab/bartel1_ata/jwnam/Project/Celegans/modEncode/Robert_Aggregate/Aggregate_1003.integrated_transcripts.ucsc_browser.ws190.txt'
    filename = genomeToFile[genomeName]
    geneList = dict()
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        raw_line = line.split('\t')
	if len(raw_line)==10: raw_line.insert(1, raw_line[0])
        name = raw_line[0]
        geneID = raw_line[1]
        chr = raw_line[2]
        sense = raw_line[3]
        txCoords = map(int,raw_line[4:6])
        cdCoords = map(int,raw_line[6:8])
        exStarts = map(int,raw_line[9].split(',')[:-1])
        exEnds = map(int,raw_line[10].split(',')[:-1])
        # fix the edges to work with the Gene specs
        #exEnds = map(lambda n: n-1, exEnds)
	exStarts = map(lambda n: n+1, exStarts)
	#exStarts[0]+=1

        txCoords = [txCoords[0], txCoords[1] ]
        cdCoords = [cdCoords[0], max([cdCoords[1], 0])]
        if cdCoords[0]!=0 or cdCoords[1]!=0:
            newGene = utilityModule.Gene(name,geneID,chr,sense,txCoords,cdCoords,exStarts,exEnds)
            if not(geneList.has_key(chr)): geneList[chr] = []
            geneList[chr].append([txCoords[0],txCoords[1],newGene])
    f.close()
    return geneList

def cmp1(a1, a2): return cmp(a1[1], a2[1])
def cmp0(a1, a2): return cmp(a1[0], a2[0])
def get_new3UTR(assembly, method, tpSeqSample):
    newUTR=dict()
    new3UTRD=dict()
    newUTR['ce6'] = '/lab/bartel1_ata/jwnam/Project/Celegans/3UTR/new3UTRcoord.txt'
    newUTR['hg19'] = '/lab/bartel1_ata/jwnam/Project/Human/DifferentialTargets/Apps/3PSeq/3PSeq_Signals_Across_Samples_15_L3UTR_All.txt'
    newUTR['GRCh37.66'] = '/lab/bartel1_ata/jwnam/Project/Human/DifferentialTargets/Apps/3PSeq/3PSeq_Signals_Across_Samples_15_L3UTR_All.txt'
    #newUTR['hg19'] = '/lab/bartel1_ata/jwnam/Project/Human/DifferentialTargets/Apps/3PSeq/3PSeq_Signals_Across_Samples_Merk_L3UTR_All.txt'
    newUTR['dm3'] = '/lab/bartel1_ata/jwnam/Project/Fly/DifferentialTargets/Apps/3PSeq/3PSeq_Signals_Across_Samples_15_L3UTR_All.txt'
    newUTR['mm9'] = '/lab/bartel1_ata/jwnam/Project/Mouse/DifferentialTargets/Apps/3PSeq/3PSeq_Signals_Across_Samples_15_L3UTR_Calvin_All.txt'
    #newUTR['mm9'] = '/lab/bartel1_ata/jwnam/Project/Mouse/DifferentialTargets/Apps/3PSeq/3PSeq_Signals_Across_Samples_15_L3UTR_All.txt'
    #newUTR['mm9'] = '/lab/bartel1_ata/jwnam/Project/Mouse/DifferentialTargets/Apps/3PSeq/3PSeq_Signals_Across_Samples_Merk_L3UTR_All.txt'
    newUTR['danRer7'] = '/lab/bartel1_ata/jwnam/Project/Zebrafish/DifferentialTargets/Apps/3PSeq/3PSeq_Signals_Across_Samples_15_L3UTR_All.txt'
    if newUTR.has_key(assembly):
    	file = open(newUTR[assembly])
    	lines = file.readlines(); file.close()
    	if assembly=='ce6':
    		for line in lines[1:]:
			tmp = line.split('\t')
			geneID = tmp[0]
			new3UTR = int(tmp[1])
			new3UTRD[geneID]=new3UTR
    	elif assembly=='hg19' or assembly=='dm3' or assembly=='mm9' or assembly=='danRer7':
	#NM_001143985    chr11   +       65771620:17,    65771620:26,    65771624:29,    65771624:23,
		title = lines[0].split('\n')[0].split('\t')[3:]
		titleD =dict(); col=3
		for t in title: titleD[t]=col; col+=1
		colNum = titleD[tpSeqSample]
		for line in lines[1:]:
			tend=-1; tend1=-1; tend2=-1
			line = line.split('\t')
			mp=[]; lp=[]
			poss = line[colNum]
			if poss.find(':')>=0:
			    p = poss.split(',')
			    p = filter(lambda x: len(x)>0, p)
			    p = map(lambda x: map(float, x.split(':')), p)
			    majorEnd = p[0][0]
			    p.sort(cmp0)
			    if method=='longest':
				if line[2]=='+': tend = p[-1][0]
				else: tend = p[0][0]
			    elif method=='major':
				if line[2]=='+': tend1 = p[-1][0]
				else: tend1 = p[0][0]
				if line[2]=='+': tend = majorEnd 
				else: tend =  majorEnd
				#print line[2], tend1, tend
			if tend>0: new3UTRD[line[0]]=tend
    return new3UTRD

def get_pseudogenes():
    filename = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerPseudoGene.txt'
    geneList = dict()
    f = open(filename)
    lines = f.readlines()
    for line in lines:
        raw_line = line.split('\t')
        name = raw_line[0]
        geneID = raw_line[1]
        chr = raw_line[2]
        sense = raw_line[3]
        txCoords = map(int,raw_line[4:6])
        cdCoords = map(int,raw_line[6:8])
        exStarts = map(int,raw_line[9].split(',')[:-1])
        exEnds = map(int,raw_line[10].split(',')[:-1])
        # fix the edges to work with the Gene specs
        #exEnds = map(lambda n: n-1, exEnds)
        txCoords = [txCoords[0], txCoords[1]]
        cdCoords = [cdCoords[0], max([cdCoords[1],0])]
        if cdCoords[0]!=0 or cdCoords[1]!=0:
            newGene = utilityModule.Gene(name,geneID,chr,sense,txCoords,cdCoords,exStarts,exEnds)
            if not(geneList.has_key(chr)): geneList[chr] = []
            geneList[chr].append([txCoords[0],txCoords[1],newGene])
    f.close()
    return geneList

def getNewRefFlatbyChrom(genomeName, method, tpSeqSample, test = lambda g: True):
    newRefFlat = get_new3UTR(genomeName, method, tpSeqSample)
    genomeToFile=dict()
    # this file was updated to ce6. It is not 2007 file.
    genomeToFile['ce6'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/refFlat.txt'
    genomeToFile['mm9'] = '/lab/bartel6_ata/nam/mouse/annotation/refFlat_mm9.txt'
    genomeToFile['dm3'] = '/lab/bartel3_ata/jwnam/d.melanogaster/annotation/refFlat.txt'
    genomeToFile['danRer6'] = '/lab/bartel3_ata/jwnam/zebrafish/refFlat.txt'
    genomeToFile['danRer7'] = '/lab/bartel3_ata/jwnam/zebrafish/danRer7/refFlat.txt'
    genomeToFile['hg18_distinct'] = '/lab/bartel3_ata/jwnam/h.sapiens/nature_refSeq_distinct.fa'
    genomeToFile['hg19'] = '/lab/bartel3_ata/jwnam/h.sapiens/hg19/refFlat.txt'
    genomeToFile['GRCh37.66'] = '/lab/bartel3_ata/jwnam/h.sapiens/hg19/GRCh37.66.genePred2'
    genomeToFile['sangerRna'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerRnaGene.txt'
    genomeToFile['sangerPseudogene'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerPseudoGene.txt'
    genomeToFile['sangerGene'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerGene.txt'
    genomeToFile['denovo_annotation']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/combined_step3.txt'
    genomeToFile['denovo_annotation_v1.3']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/combined_step3_v1.3.txt'
    genomeToFile['combined']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/newTest3P_directCombined.txt'
    genomeToFile['modEncode_Aggregate']='/lab/bartel1_ata/jwnam/Project/Celegans/modEncode/Robert_Aggregate/Aggregate_1003.integrated_transcripts.ucsc_browser.ws190.txt'
    filename = genomeToFile[genomeName]
    geneList = dict()
    f = open(filename)
    lines = f.readlines()
    updatedUTRNum=0
    updatedUTRNum_100D=0
    for line in lines:
        raw_line = line.split('\t')
	if len(raw_line)==10: raw_line.insert(1, raw_line[0])
        name = raw_line[0]
        geneID = raw_line[1]

        #///////////
	newEnd = int(newRefFlat.get(geneID,-1))
	
        chr = raw_line[2]
        sense = raw_line[3]
        txCoords = map(int,raw_line[4:6]) 
        cdCoords = map(int,raw_line[6:8])
        exStarts = map(int,raw_line[9].split(',')[:-1])
        exEnds = map(int,raw_line[10].split(',')[:-1])
        # fix the edges to work with the Gene specs
        #exEnds = map(lambda n: n-1, exEnds)

	#print geneID, sense, txCoords,
	if newEnd>0:
	   if sense=='+':
              txCoords = [txCoords[0], newEnd]
	      #exEnds[-1] = max(exEnds[-1],newEnd)
	      if abs(exEnds[-1]-newEnd)>=100: updatedUTRNum_100D+=1
	      if abs(exEnds[-1]-newEnd)>=1: updatedUTRNum+=1
	      exEnds[-1] = newEnd
	   else:
              txCoords = [ newEnd, txCoords[1]]
	      if abs(exStarts[0]-newEnd)>=100: updatedUTRNum_100D+=1
	      if abs(exStarts[0]-newEnd)>=1: updatedUTRNum+=1
	      #exStarts[0] = min(exStarts[0],newEnd)
	      exStarts[0] = newEnd
	#print txCoords
        cdCoords = [cdCoords[0], max([cdCoords[1],0])]
        if cdCoords[0]!=0 or cdCoords[1]!=0:
            newGene = utilityModule.Gene(name,geneID,chr,sense,txCoords,cdCoords,exStarts,exEnds)
            if not(geneList.has_key(chr)): geneList[chr] = []
            geneList[chr].append([txCoords[0],txCoords[1],newGene])
    f.close()
    print '#Updated 3UTR Number: ' + str(updatedUTRNum)
    print '#Updated 3UTR Number(>=100): ' + str(updatedUTRNum_100D)
    return geneList 

def getNewRefFlat(genomeName, method, tpSeqSample, test = lambda g: True):
    newRefFlat = get_new3UTR(genomeName, method, tpSeqSample)
    genomeToFile=dict()
    genomeToFile['ce6'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/refFlat.txt'
    genomeToFile['danRer6'] = '/lab/bartel3_ata/jwnam/zebrafish/refFlat.txt'
    genomeToFile['danRer7'] = '/lab/bartel3_ata/jwnam/zebrafish/danRer7/refFlat.txt'
    genomeToFile['dm3'] = '/lab/bartel3_ata/jwnam/d.melanogaster/annotation/refFlat.txt'
    genomeToFile['mm9'] = '/lab/bartel6_ata/nam/mouse/annotation/refFlat_mm9.txt'
    genomeToFile['hg18_distinct'] = '/lab/bartel3_ata/jwnam/h.sapiens/nature_refSeq_distinct.fa'
    genomeToFile['hg19'] = '/lab/bartel3_ata/jwnam/h.sapiens/hg19/refFlat.txt'
    genomeToFile['GRCh37.66'] = '/lab/bartel3_ata/jwnam/h.sapiens/hg19/GRCh37.66.genePred2'
    genomeToFile['sangerRna'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerRnaGene.txt'
    genomeToFile['sangerPseudogene'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerPseudoGene.txt'
    genomeToFile['sangerGene'] = '/lab/bartel3_ata/jwnam/c.elgans_may_2008/annotation/sangerGene.txt'
    genomeToFile['denovo_annotation']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/combined_step3.txt'
    genomeToFile['denovo_annotation_v1.3']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/combined_step3_v1.3.txt'
    genomeToFile['combined']='/lab/solexa_bartel1/jwnam/RNASeq/Celegans/Combined_TophatOutput/corrected/gtfs/newTest3P_directCombined.txt'
    genomeToFile['modEncode_Aggregate']='/lab/bartel1_ata/jwnam/Project/Celegans/modEncode/Robert_Aggregate/Aggregate_1003.integrated_transcripts.ucsc_browser.ws190.txt'
    filename = genomeToFile[genomeName]
    geneList = dict()
    f = open(filename)
    lines = f.readlines()
    nnum=0
    updatedUTRNum=0
    updatedUTRNum_100D=0
    for line in lines:
        raw_line = line.split('\t')
	if len(raw_line)==10: raw_line.insert(1, raw_line[0])
        name = raw_line[0]
	if len(name)==0: nnum+=1; name = str(nnum)
        geneID = raw_line[1]
	if genomeName=='sangerGene' or genomeName=='sangerPseudogene' or genomeName=='sangerRna':
		name = geneID
        #///////////
        newEnd = int(newRefFlat.get(geneID,-1))

        chr = raw_line[2]
        sense = raw_line[3]
        txCoords = map(int,raw_line[4:6])
        cdCoords = map(int,raw_line[6:8])
        exStarts = map(int,raw_line[9].split(',')[:-1])
        exEnds = map(int,raw_line[10].split(',')[:-1])
        # fix the edges to work with the Gene specs
        exEnds = map(lambda n: n-1, exEnds)

        #print geneID, sense, txCoords,
        if newEnd>0:
           if sense=='+':
              txCoords = [txCoords[0], newEnd]
              #exEnds[-1] = max(exEnds[-1],newEnd)
              exEnds[-1] = newEnd
	      if abs(exEnds[-1]-newEnd)>=100: updatedUTRNum_100D+=1
	      if abs(exEnds[-1]-newEnd)>=1: updatedUTRNum+=1
           else:
              txCoords = [newEnd, txCoords[1]]
              #exStarts[0] = min(exStarts[0],newEnd)
              exStarts[0] = newEnd
	      if abs(exStarts[0]-newEnd)>=100: updatedUTRNum_100D+=1
	      if abs(exStarts[0]-newEnd)>=1: updatedUTRNum+=1
        #print txCoords
        cdCoords = [cdCoords[0], max([cdCoords[1],0])]
        if cdCoords[0]!=0 or cdCoords[1]!=0:
            newGene = utilityModule.Gene(name,geneID,chr,sense,txCoords,cdCoords,exStarts,exEnds)
            if not(geneList.has_key(geneID)): geneList[geneID] = newGene
	    else:
		preGene = geneList[geneID]
		geneLen = preGene.txLocus().end() - preGene.txLocus().start()
		geneLen2 = txCoords[1]-txCoords[0]
		if geneLen2>geneLen: geneList[geneID] = newGene
    f.close()
    print '#Updated 3UTR Number: ' + str(updatedUTRNum)
    print '#Updated 3UTR Number(>=100): ' + str(updatedUTRNum_100D)
    return geneList


def get_seq(gene): #'ORF', '5UTR', '3UTR'
    loci=''
    cdsloci = gene.cdExons() 
    utr5loci = gene.fpExons(gene.sense())
    utr3loci = gene.tpExons(gene.sense())
    utr5seqLen=0;utr3seqLen=0
    numOfLoci = len(loci);interval=0;pre_interval=0
    for locus in utr5loci: utr5seqLen += (locus.end()-locus.start() +1)
    for locus in utr3loci: utr3seqLen += (locus.end()-locus.start() +1)
    return utr5seqLen,utr3seqLen

def get_genomePos(gene, start2, end2, type='ORF'): #'ORF', '5UTR', '3UTR'
    loci=''
    if type=='ORF': loci = gene.cdExons() 
    elif type=='5\'UTR': loci = gene.fpExons(gene.sense())
    elif type=='3\'UTR': loci = gene.tpExons(gene.sense())
    else: print type + ' error'
    n_end=[];n_start=[];seqLen=0
    numOfLoci = len(loci);interval=0;pre_interval=0
    for locus in loci:
	seqLen += (locus.end()-locus.start() +1)
    start=0;end=0;add=0;add2=0
    if numOfLoci>0 and loci[0].sense()=='-':start=seqLen-end2+1;end=seqLen-start2+1
    else: start=start2;end=end2-1
    #print gene.sense(), numOfLoci, seqLen
    for i in xrange(numOfLoci):
    	ex = loci[i]
    	#print ex.start(), ex.end()
    	pre_interval = interval; residue1 = start - pre_interval; residue2 = end - pre_interval
	if gene.sense()=='-': add=1; 
    	if residue1 < ex.end()-ex.start() and residue2 < ex.end()-ex.start():
	    n_start.append(ex.start() + (residue1)); n_end.append(ex.start() + (residue2)+1-add);break
    	elif residue1 <= ex.end()-ex.start() and residue2 >= ex.end()-ex.start():
	    n_start.append(ex.start() + (residue1)); n_end.append(ex.end()+add)
	    if (numOfLoci>i+1): n_start.append(loci[i+1].start()-1); n_end.append(loci[i+1].start() + (residue2-(ex.end()-ex.start())))
	    break
    	else: interval += (ex.end()-ex.start()+1)
        #print n_start, n_end
    return n_start, n_end

def getAlignment(gene, species, n_start, n_end):
    chromosome = gene.chr()
    sense = gene.sense()
    if species=='briggsae': sp='cb3'
    if species=='brenneri':sp='caePb2'
    if species=='remanei':sp='caeRem3'
    if species=='japonica':sp='caeJap1'
    if species=='pacificus':sp='caePac1'
    ali_fileName = '/lab/bartel/jwnam/c.elgans_may_2008/genome/alignment/' + chromosome+'.ce6.'+ sp + '.net.axt'
    seq=[];pos=[] 
    ali_file = open(ali_fileName)
    alignments = ali_file.readlines()
    alignments = filter(lambda x: x[0]!='#' and len(x)>10, alignments)
    #alignments=all_alignments[species+'_'+chromosome]
    linelen = len(alignments) 

    def check_line(line, npos, start, end):
	hipen=0;k=1;adj=0
	count=int(npos)-1; pos=[0,0]; seq='';linelen = len(line)
	for i in xrange(linelen):
	    if line[i]!='-': count+=1; 
	    #count+=1
	    if count >= start and count <=end and line[i]!='-': seq+=line[i]; 
	    if count >= start and count <=end and line[i]=='-': hipen+=1
	    if count == start: pos[0]=i+1
	    if count == end: pos[1]=i-hipen+1;break
	return seq.upper(),pos

    def get_otherSeq(line, start, end):
	frag = line[start-1:end-1];n_frag='';frag_len=len(frag)
	for i in xrange(frag_len):
	    if frag[i]!='-': n_frag+=frag[i]
	return n_frag.upper()

    elegans_seq='';elegans_seq2='';other_seq='';other_seq2='';flag=False
    num_start = len(n_start)
    for j in xrange(num_start):
        for i in xrange(linelen):
	    align = alignments[i]
	    if len(align.split(' '))>3:
	        pos = align.split(' ')[2:4]
	        if int(pos[0]) < n_start[j] and int(pos[1])>n_end[j]:
		    elegans_seq,al_pos = check_line(alignments[i+1],pos[0],n_start[j],n_end[j])
		    other_seq = get_otherSeq(alignments[i+2],al_pos[0], al_pos[1]+1)
		    elegans_seq2+=elegans_seq
		    other_seq2+=other_seq
		    #print alignments[i+1]
		    #print elegans_seq, other_seq, al_pos
		    break
	    elif int(pos[0]) > n_start[j]: break
	    if flag==True: break
    ali_file.close()
    if gene.sense()=='-': elegans_seq2 = utilityModule.reverseComp(elegans_seq2); other_seq2 = utilityModule.reverseComp(other_seq2)
    return elegans_seq2, other_seq2
