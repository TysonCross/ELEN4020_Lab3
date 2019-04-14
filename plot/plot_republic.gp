# gnuplot
# Tyson Cross
# ELEN4020

reset

# qt
#set terminal qt size 600,400  enhanced font "Helvetica,16" persist

#eps
set terminal pdf size 6.0,4.0 enhanced color \
font 'Helvetica,10' linewidth 2
set output 'plot_republic.pdf'
set encoding utf8

# Color definitions
set colorsequence default

# Styles
set border linewidth 1.8
set style fill solid 1.00 noborder
set for [i=1:7] linetype i dashtype i
set style histogram
set style data histogram

# Titles
set title "Top Word Frequency in 'The Republic" font ",18"
#set ylabel "Frequency" offset 1.1 font "Helvetica-Oblique,18"
#set xlabel "Words" offset 0,0.6 font "Helvetica-Oblique,18"

# Axes
# remove border on top and right and set color to gray
set style line 11 lc rgb '#808080' lt 1
unset xtics
set border 2 back ls 11
set ytics nomirror out scale 1.25 font ", 10" offset 0.75
set size 1.0,1.0
set origin 0.0,0.0

# Grid
set grid nopolar
set grid y
set auto y
set grid noxtics nomxtics ytics nomytics noztics nomztics nortics nomrtics \
 nox2tics nomx2tics noy2tics nomy2tics nocbtics nomcbtics
set grid layerdefault   lt 0 linecolor 0 linewidth 0.500,  lt 0 linecolor 0 linewidth 0.500

# labels
set key off
set style increment default
set style histogram clustered gap 2 title textcolor lt -1 font ",18"  offset character 2, -2
set datafile missing '-'
set style data histograms
set xtics border in scale 1,0.5 mirror font ", 10" rotate by -45  autojustify
set xtics  norangelimit 
set xtics   ()
set xtic noenhanced
set xrange [ * : * ] noreverse writeback
set x2range [ * : * ] noreverse writeback
set yrange [ * : * ] noreverse writeback
set y2range [ * : * ] noreverse writeback
set zrange [ * : * ] noreverse writeback
set cbrange [ * : * ] noreverse writeback
set rrange [ * : * ] noreverse writeback

plot "../output/output_republic.txt" using 1:xticlabels(2) with histogram linecolor rgb "#6BA5D5"
