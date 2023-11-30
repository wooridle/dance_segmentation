import musicsections
import pickle
import glob
import os

deepsim_model_folder = "./models/deepsim/"
fewshot_model_folder = "./models/fewshot/"

model_deepsim = musicsections.load_deepsim_model(deepsim_model_folder)
model_fewshot = musicsections.load_fewshot_model(fewshot_model_folder)

audio_files = glob.glob("./audio_files/*")

for audio_file in audio_files:

    segmentations, features = musicsections.segment_file(
        audio_file, 
        deepsim_model=model_deepsim,
        fewshot_model=model_fewshot,
        min_duration=8,
        mu=0.5,
        gamma=0.5,
        beats_alg="madmom",
        beats_file=None)


    filename, file_extension = os.path.splitext(audio_file)

    audio_filename = os.path.basename(filename)

    with open(f'./pickle_data/{audio_filename}.pickle' , 'wb') as f:
        pickle.dump(segmentations, f, pickle.HIGHEST_PROTOCOL)
    print(segmentations)
    print(features)
# musicsections.plot_segmentation(segmentations)
