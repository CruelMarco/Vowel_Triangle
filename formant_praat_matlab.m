tic;
BaseDir='"C:\Users\Spirelab\Desktop\Vowel_Triangle\subject_wise_with_noise\White\';
WavDir = [BaseDir 'Audio_SNR_5\'];
BoundDirH = [BaseDir 'Anote\'];
FormantDir = [BaseDir 'Formant_mean_SNR_5\'];
PraatLocation='C:\Laptop_data\Praat\Praat.exe';
PraatScript='formants.praat';
Sounds = {'aaa\\"','eee\\"','uuu\\"'};
%praatcommand = [PraatLocation ' ' '--run' ' ' PraatScript ' ' WavDir ' ' BoundDirH  ' ' FormantDir];

praatcommand = [PraatLocation ' ' '--run' ' ' PraatScript ];
% for i=1:length(Sounds)
% %praatcommand = [PraatLocation ' ' '--run' ' ' PraatScript ' ' WavDir cell2mat(Sounds(i)) ' ' BoundDirH cell2mat(Sounds(i)) ' ' FormantDir cell2mat(Sounds(i))];
% praatcommand = [PraatLocation ' ' '--run' ' ' PraatScript ' ' WavDir (Sounds(i)) ' ' BoundDirH cell2mat(Sounds(i)) ' ' FormantDir cell2mat(Sounds(i))];
% retval=system(praatcommand);
% end
retval=system(praatcommand);
disp("Finished Extracting Formants");
toc;