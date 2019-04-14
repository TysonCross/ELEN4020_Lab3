# gnuplot
# Tyson Cross
# ELEN4020

reset

# qt
#set terminal qt size 600,400  enhanced font "Helvetica,16" persist

#eps
set terminal pdf size 6.0,4.0 enhanced color \
font 'Helvetica,10' linewidth 2
set output 'plot_hamlet.pdf'

# Color definitions
set colorsequence default

# Styles
set border linewidth 1.8
set style fill solid 1.00 noborder
set for [i=1:7] linetype i dashtype i
set style histogram
set style data histogram

# Titles
set title "Top Word Frequency in 'Hamlet'" font ",18"
#set ylabel "Frequency" offset 1.1 font "Helvetica-Oblique,18"
#set xlabel "Words" offset 0,0.6 font "Helvetica-Oblique,18"

# Axes
# remove border on top and right and set color to gray
set style line 11 lc rgb '#808080' lt 1
unset xtics
set border 3 back ls 11
set ytics nomirror out scale 1.25 font ", 10" offset 0.5
set xtics nomirror out scale 1.25 font ", 10" offset 0,0.5 rotate by -45
set size 1.0,1.0
set origin 0.0,0.0

# Grid
#set style line 12 lc rgb'#808080' lt 0 lw 0.7
#set grid back ls 12
#unset grid
set grid y
set auto y

# labels
set xtics border in scale 1,0.5 nomirror rotate by -90 offset character 0, 0, 0
set key off

#set multiplot
plot "../output/output_hamlet.txt" using 1:xticlabels(2) with histogram linecolor rgb "#6BA5D5"
#unset multiplot

set encoding utf8
     
