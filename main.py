import argparse
import asone
from asone import ASOne
import argparse

def main(args):
    dt_obj = ASOne(
        tracker=asone.BYTETRACK,
        detector=asone.YOLOX_DARKNET_PYTORCH,
        use_cuda=args.use_cuda
        )
    for bbox_details, frame_details in dt_obj.track_video(
                                                            args.video_path,
                                                            output_dir=args.output_dir,
                                                            save_result=args.save_result,
                                                            display=args.display
                                                            ):
        # bbox_details = bbox_xyxy, ids, scores, class_ids
        # frame_details = frame, frame_no, fps
        
        pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('video_path', help='Path to input video')
    parser.add_argument('--cpu', default=True, action='store_false', dest='use_cuda',
                        help='run on cpu if not provided the program will run on gpu.')
    parser.add_argument('--no_save', default=True, action='store_false',
                        dest='save_result', help='if provided the results will not save.')
    parser.add_argument('--no_display', default=True, action='store_false',
                        dest='display', help='if provided the results will not be displayed on screen')
    parser.add_argument('--output_dir', default='data/results',  help='Path to output directory')
    
    args = parser.parse_args()

    main(args)