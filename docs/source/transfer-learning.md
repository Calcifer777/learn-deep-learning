# Transfer Learning

Transfer learning involves taking a model, or parts of a model, that is trained for one task, and then using it to solve a different, but related, task. The idea is that some of the skills learned for the original task carry over (transfer) and are applicable to the new task.

When training begins, the layers from the pretrained model have already been trained for many epochs on a large dataset, whereas the weights in the final layers are completely random.

Therefore, it is often a good idea to freeze these weights and only train the newly added layers.

One powerful technique is to do pretraining of a model using an unsupervised learning technique that does not require labeled data. Large amounts of unlabeled data are much easier to obtain than labeled data.