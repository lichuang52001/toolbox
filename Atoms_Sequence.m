% -----------------------------------
% Author : Chuang Li
% Date : June 5, 2018
% Purpose : Calculate the mean energy of certain lattice containing A atom(No: m) and B atom (No: n) in random sequence
% -----------------------------------

%% Parameter setting
m = 5 ;    % set the number of A atom
n = 10 ;     % set the number of B atom
energy00 = 1 ;    % the energy bewteen A-A
energy01 = 2 ;    % the energy between A-B
energy11 = 3 ;    % the energy between B-B


numallposscond = nchoosek(m+n,n) ;    %  num of all possoble conditions
v_matrix = [1:m+n] ;
k_matrix = nchoosek(v_matrix,n) ;     % determine all the locations of B atoms

main_matrix = zeros(numallposscond, m+n) ;  % the main matrix
for i = 1:numallposscond
    for j = 1:n
        main_matrix(i, k_matrix(i,j)) = 1 ;   % all the B atoms are represented by 1, meanwhile A atoms is 0
    end
end

energy = zeros(numallposscond,1) ;    % this matrix store the energy of every possible conditions

for i = 1:numallposscond
    for j = 1:m+n-1
        if main_matrix(i,j) == 0
            if main_matrix(i,j+1) == 0
                energy(i,1) = energy(i,1)+energy00 ;
            else
                energy(i,1) = energy(i,1)+energy01 ;
            end
        else
            if main_matrix(i,j+1) == 1
                energy(i,1) = energy(i,1)+energy11 ;
            else
                energy(i,1) = energy(i,1)+energy01 ;
            end
        end
    end
end

% save energy.dat energy -ascii
mine = min(energy) ;
maxe = max(energy) ;
% 求三个energy的最大公约数
gongyue = 1 ;
xcor = [mine:gongyue: maxe]' ;
[numrow, numcol] = size(xcor) ;
numenergy = zeros(numrow,1) ;
for i = 1:numrow
    numenergy(i,1) = sum(energy(:)==xcor(i,1)) ;
end
bar(xcor, numenergy)


for i = 1:numallposscond
    modmod(i,1) = mod(energy(i,1),0.1) ;
end

            



