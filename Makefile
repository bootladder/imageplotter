.PHONY : always
.SECONDARY :
all : help target_floor1 #target_floor2

always: 

help : 
	@echo Starting Build.
	@echo Generating images for all floors
	@echo Each directory contains datasets, an image , and a map
	@echo "\n"

FLOOR1_RAW_DATASETS = $(shell ls floor1/*.rawdata.csv)

FLOOR1_DATASETS := $(basename $(FLOOR1_RAW_DATASETS))
FLOOR1_DATASETS := $(basename $(FLOOR1_DATASETS))
FLOOR1_DATASETS := $(addsuffix .locationdata.csv , $(FLOOR1_DATASETS) )

%.rawdata.csv : always

%.parsedrawdata.csv : %.rawdata.csv always
	@echo MAKING PARSED RAW DATA
	python snifferfilterparser.py --outdata $@ --indata $<

%.locationdata.csv : %.parsedrawdata.csv always 
	@echo MAKING LOCATION DATA FILE!!!
	@echo making target: $@ with prereq: $<
	python location2plotter.py --outdata $@ --indata $< --map $(dir $<)map.csv



target_floor1: $(FLOOR1_DATASETS) 
	@echo datasets are $(FLOOR1_DATASETS)
	@echo making floor1 images.  List of images is : $^
	for file in $^ ; do \
		s=$${file##*/} ; \
		s=$${s%.*} ;  \
		python imageplotter.py --image floorplan1.jpg --data $${file} --outimage floor1/$${s}.jpg ;\
	done

target_floor2: $(FLOOR2_DATASETS)
	@echo 
	@echo making floor2 images.  List of images is : $^
	for file in $^ ; do \
		s=$${file##*/} ; \
		s=$${s%.*} ;  \
		python imageplotter.py --image floorplan2.jpg --data $${file} --outimage floor2/$${s}.jpg ;\
	done
















#	for file in $^ ; do \
#		python imageplotter.py --image floorplan2.jpg --data $${file}_image1 ;\
#	done






#floor3/%.csv : atrg
#	@echo hello777
#	@echo hello777
#	@echo hello777
#	@echo hello777
#	@echo hello777
#	@echo hello777
#
#floor1/%loor1_trial0.locationdata.csv : argh
#	@echo hello111
#	@echo hello111
#	@echo hello111
#	@echo hello111
#	@echo hello111
#	@echo hello111
#	@echo hello111
#
#floor2/%.data.csv : atrg
#	@echo hello111
