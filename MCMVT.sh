MCMT_CONFIG_FILE="aic.yml"

cd ./detector/yolo/
python gen_images_aic.py "aic.yml"

./gen_det.sh

cd ./../../

cd ./reid_bidir/
python extract_image_feat.py "aic_reid1.yml"
python extract_image_feat.py "aic_reid2.yml"
python extract_image_feat.py "aic_reid3.yml"
python merge_reid_feat.py ${MCMT_CONFIG_FILE}

#### MOT ####
cd ../tracker/MOTBaseline
sh run_aic.sh ${MCMT_CONFIG_FILE}

#### MCMVT ####
cd ../../reid_bidir/reid-matching/tools
python trajectory_fusion.py ${MCMT_CONFIG_FILE}
python sub_cluster.py ${MCMT_CONFIG_FILE}
python gen_res.py ${MCMT_CONFIG_FILE}
python interpolation.py ${MCMT_CONFIG_FILE}

cd /home/ec2-user/MCMVT/post_processing
python annotate.py "/home/ec2-user/MCMVT/datasets/detection/images/test" "S06" "c041" "/home/ec2-user/MCMVT/reid_bidir/reid-matching/tools/track1.txt"
python annotate.py "/home/ec2-user/MCMVT/datasets/detection/images/test" "S06" "c042" "/home/ec2-user/MCMVT/reid_bidir/reid-matching/tools/track1.txt"
python annotate.py "/home/ec2-user/MCMVT/datasets/detection/images/test" "S06" "c043" "/home/ec2-user/MCMVT/reid_bidir/reid-matching/tools/track1.txt"
python annotate.py "/home/ec2-user/MCMVT/datasets/detection/images/test" "S06" "c044" "/home/ec2-user/MCMVT/reid_bidir/reid-matching/tools/track1.txt"
python annotate.py "/home/ec2-user/MCMVT/datasets/detection/images/test" "S06" "c045" "/home/ec2-user/MCMVT/reid_bidir/reid-matching/tools/track1.txt"
python annotate.py "/home/ec2-user/MCMVT/datasets/detection/images/test" "S06" "c046" "/home/ec2-user/MCMVT/reid_bidir/reid-matching/tools/track1.txt"


python images-to-video.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c041/output/" "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c041/output/video/c041.mp4"
python images-to-video.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c042/output/" "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c042/output/video/c042.mp4"
python images-to-video.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c043/output/" "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c043/output/video/c043.mp4"
python images-to-video.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c044/output/" "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c044/output/video/c044.mp4"
python images-to-video.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c045/output/" "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c045/output/video/c045.mp4"
python images-to-video.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c046/output/" "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c046/output/video/c046.mp4"


python upload-images-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c041/output/" "traffic-analysis" "output/c041"
python upload-images-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c042/output/" "traffic-analysis" "output/c042"
python upload-images-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c043/output/" "traffic-analysis" "output/c043"
python upload-images-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c044/output/" "traffic-analysis" "output/c044"
python upload-images-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c045/output/" "traffic-analysis" "output/c045"
python upload-images-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c046/output/" "traffic-analysis" "output/c046"

python upload-video-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c041/output/video/c041.mp4" "traffic-analysis" "output/S06/videos"
python upload-video-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c042/output/video/c042.mp4" "traffic-analysis" "output/S06/videos"
python upload-video-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c043/output/video/c043.mp4" "traffic-analysis" "output/S06/videos"
python upload-video-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c044/output/video/c044.mp4" "traffic-analysis" "output/S06/videos"
python upload-video-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c045/output/video/c045.mp4" "traffic-analysis" "output/S06/videos"
python upload-video-to-s3.py "/home/ec2-user/MCMVT/datasets/detection/images/test/S06/c046/output/video/c046.mp4" "traffic-analysis" "output/S06/videos"