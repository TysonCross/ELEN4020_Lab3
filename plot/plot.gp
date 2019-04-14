# gnuplot
# Tyson Cross
# ELEN4020

reset

# qt
#set terminal qt size 600,400  enhanced font "Helvetica,16" persist

#eps
set terminal pdf size 6.0,4.0 enhanced color \
font 'Helvetica,10' linewidth 2
set output 'gnuplot/plot.pdf'

# color definitions
set border linewidth 1.8

set colorsequence default
set for [i=1:7] linetype i dashtype i

# Titles
set title "Word Frequency" font ",18"
#set ylabel "Frequency" offset 1.1 font "Helvetica-Oblique,18"
#set xlabel "Words" offset 0,0.6 font "Helvetica-Oblique,18"

# Axes
# remove border on top and right and set color to gray
set style line 11 lc rgb '#808080' lt 1
set border 3 back ls 11
set ytics nomirror out scale 1.25 font ", 10" offset 0.5
set xtics nomirror out scale 1.25 font ", 10" offset 0,0.5
set size 1.0,1.0
set origin 0.0,0.0

# Grid
#set style line 12 lc rgb'#808080' lt 0 lw 0.7
#set grid back ls 12
#unset grid

# labels
set xtics border in scale 1,0.5 nomirror rotate by -90 offset character 0, 0, 0
set key off

#set multiplot
plot "output.txt" using 1:xticlabels(2) with histogram
#unset multiplot

set encoding utf8
     
