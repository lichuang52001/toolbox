clear all
close all

mov = VideoWriter('test.avi') ;
open(mov) ;

num = 200 ;

x = linspace(1, num,num) ;
y = x + 10*rand(1,num) ;

t = 0 ;
for t = 1:num 
    plot(x(1,1:t),y(1,1:t),'.','MarkerEdgeColor','k','MarkerSize',10)
    hold on
    plot(x(1,1:t),y(1,1:t),'k')
    xlim([min(x)-10 max(x)+10]) ;
    ylim([min(y)-5 max(y)+5]) ;
    pause(0.1)
    frame = getframe(gcf) ;
    writeVideo(mov,frame) ;
end

close(mov)
