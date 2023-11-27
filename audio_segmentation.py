import musicsections

deepsim_model_folder = "./models/deepsim/beat.h5"
fewshot_model_folder = "./models/fewshot/best_model.tar"

model_deepsim = musicsections.load_deepsim_model(deepsim_model_folder)
model_fewshot = musicsections.load_fewshot_model(fewshot_model_folder)

audiofile = "./dance_audio.mp3"

segmentations, features = musicsections.segment_file(
    audiofile, 
    deepsim_model=model_deepsim,
    fewshot_model=model_fewshot,
    min_duration=8,
    mu=0.5,
    gamma=0.5,
    beats_alg="madmom",
    beats_file=None)

print(segmentations)
print(features)
# musicsections.plot_segmentation(segmentations)