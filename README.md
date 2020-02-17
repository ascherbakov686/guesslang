

# run on my own dataset:

$ python3 -W ignore make_keywords.py /home/shcherbakov_al/guesslang/datasets/learn ./keywords.json

17:07:58 __main__ INFO Reading files form /home/shcherbakov_al/guesslang/datasets/learn

1

/home/shcherbakov_al/guesslang/datasets/learn/index.html.python

2

/home/shcherbakov_al/guesslang/datasets/learn/index.html.php

17:07:58 __main__ INFO 9 unique terms found

17:07:58 __main__ INFO 11 keywords written into keywords.json



# learn attempt

$ ~/.local/bin/guesslang --learn datasets/learn --model guesslang/data/model/

18:09:21 guesslang.guesser INFO Extract training data

18:09:21 guesslang.guesser INFO Start learning

18:09:21 guesslang.guesser INFO Step 20.00%

2020-02-17 18:09:22.691978: I tensorflow/core/platform/cpu_feature_guard.cc:140] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA

18:09:23 guesslang.guesser WARNING * Underfit! Accuracy: 50.00%

18:09:23 guesslang.guesser INFO Step 40.00%

18:09:25 guesslang.guesser WARNING * Underfit! Accuracy: 50.00%

18:09:25 guesslang.guesser INFO Step 60.00%

18:09:27 guesslang.guesser WARNING * Underfit! Accuracy: 50.00%

18:09:27 guesslang.guesser INFO Step 80.00%

18:09:29 guesslang.guesser WARNING * Underfit! Accuracy: 50.00%

18:09:29 guesslang.guesser INFO Step 100.00%

18:09:31 guesslang.guesser WARNING * Underfit! Accuracy: 50.00%

18:09:31 guesslang.__main__ INFO Guessing learning accuracy is 50.00%


