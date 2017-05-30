
all : help floor1 floor2

help : 
	@echo Generating images for all floors
	@echo Each directory contains datasets, an image , and a map

FLOOR1_DATASETS = $(shell ls floor1/*locationdata.csv)
FLOOR2_DATASETS = $(shell ls floor2/*locationdata.csv)


%.csv : atrg
	@echo hello777

%.data.csv : atrg
	@echo hello111

floor2/%.data.csv : atrg
	@echo hello111

floor1: $(FLOOR1_DATASETS)
	@echo datasets are $(FLOOR1_DATASETS)
	@echo making floor1 images.  List of images is : $^
	for file in $^ ; do \
		s=$${file##*/} ; \
		s=$${s%.*} ;  \
		python imageplotter.py --image floorplan1.jpg --data $${file} --outimage floor1/$${s}.jpg ;\
	done

floor2: $(FLOOR2_DATASETS)
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



