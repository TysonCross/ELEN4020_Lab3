# gnuplot
# Tyson Cross
# ELEN4020

reset

# qt
#set terminal qt size 600,400  enhanced font "Helvetica,16" persist

#eps
set terminal pdf size 6.0,4.0 enhanced color \
font 'CMU Serif,10' linewidth 2
set output 'plot_search_all.pdf'
set encoding utf8

# Color definitions
set colorsequence default

# Styles
set style line 1 \
    linecolor rgb '#6BA5D5' \
    linetype 1 linewidth 0.8 \
    pointtype 7 pointsize 0.2
set border linewidth 1.8
set style fill solid 1.00 noborder
set for [i=1:7] linetype i dashtype i
# set style histogram
# set style data histogram

# Titles
#set title "Top 1000 Words Frequencies in 'In Search of Lost Time'" font ",18"
#set ylabel "Frequency" offset 1.1 font "CMU Serif-Italic,18"
#set xlabel "Words" offset 0,0.6 font "CMU Serif-Italic,18"

# Axes
# remove border on top and right and set color to gray
set logscale xy
set style line 11 lc rgb '#808080' lt 1
unset xtics
set border 3 back ls 11
set ytics nomirror out scale 1.25 font ", 12" offset 0.5
set xtics nomirror out scale 1.25 font ", 4" offset 0,0.5
unset xtics
set size 1.0,1.0
set origin 0.0,0.0

# Grid
#set style line 12 lc rgb'#808080' lt 0 lw 0.7
#set grid back ls 12
#unset grid
set grid y
set auto y

# labels
set xtics border in scale 1,0.5 nomirror rotate by 0 offset character 0, 0, 0
set key off
set bmargin 6

# Plot
plot "../output/output_search_all.txt" using 1 with lines ls 1

