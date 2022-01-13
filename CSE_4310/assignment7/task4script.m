g= [1:30]*10;
data_file = 'scrambled_mnist10000.bin';
i=1;
for d = g
   [accuracy, confusion_matrix] = pca_classifier_stats(data_file, d);
   fprintf('%f is the accuracy when using %i number of eigenvectors. \n', accuracy, d);
end