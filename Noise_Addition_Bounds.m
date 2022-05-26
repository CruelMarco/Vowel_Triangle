path = 'C:\Users\Spirelab\Desktop\Vowel_Triangle\MatCode' ; 
dirinfo = dir;
folders = {dirinfo.name}';
folders =folders(~ismember(folders,{'.','..'}));
direc = {dirinfo.folder}' ; 
direc = string(direc);
slash = '\';
folder_dir_list = [];

SNR = 15;

dest_path = 'C:\Users\Spirelab\Desktop\Vowel_Triangle\subject_wise_with_noise\White';
for i = 1:length(folders)
    
    folders{i}
    
    temp = append(slash,folders{i});
    
    folder_dir = append(direc{1},temp);
    
    folder_dir_list{end+1} = {folder_dir};
    
    fold_dir = string(folder_dir_list);
    
    for k = 1:length(fold_dir)
        
        temp1 = dir(fold_dir(k));
        
        content = {temp1.name}';
        
        content = content(~ismember(content,{'.','..'}));
        
        TF = contains(content,'bounds', 'IgnoreCase',true);
        
        annot_Files = [];
        
        annot_Files = content(TF);
        
        annot_Files = string(annot_Files);
        
        for j = 1:length(annot_Files)
            
             annot = annot_Files(j)
           
             %copy_loc = strcat(dest_path,slash,slash,wavfiles(j))

             %file_name = [annot{1}(1:end-4) 'SNR' '_' num2str(SNR) '.txt']
             
             file_name = annot{1}

             %copy_loc = fullfile(dest_path,folders(i),file_name)
             
             src_loc = string(fullfile(direc,file_name));
           
             source = src_loc(1)
             
             copy_loc = fullfile(dest_path)
             
             location = string(copy_loc)
             
             copyfile(source,location)
                
        end
        
    end
   
end

    


% folder_dir_list = string(folder_dir_list)'
% % info = dir(folder_dir_list(1))
% % temp1 = {info.name}'
% % temp1 = temp1(~ismember(temp1,{'.','..'}))
% 
% 
% 
% for k = 1:length(folder_dir_list)
%     
%     temp1 = dir(folder_dir_list(k));
%     
%     content = {temp1.name}';
%     
%     content = content(~ismember(content,{'.','..'}))
%     
%     TF = contains(content,'.wav', 'IgnoreCase',true);
%      
%      wavfiles = content(TF);
%      
%      wavfiles = string(wavfiles)
%      
%      for j = 1:length(wavfiles)
%          
%          [y,fs] = audioread(wavfiles(j));
%          
%          noisy_y = awgn(y,SNR,'measured');
%          
%          copy_loc = strcat(dest_path,slash,folders(i),slash,wavfiles(j))
%          
%          
%          audiowrite(copy_loc , noisy_y, fs)
%          
%        
%          
%      end
% end

