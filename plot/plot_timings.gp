# gnuplot
# Tyson Cross
# ELEN4020

reset

# qt
#set terminal qt size 600,400  enhanced font "Helvetica,16" persist

#eps
set terminal pdf size 6.0,4.0 enhanced color \
font 'Helvetica,10' linewidth 2
set output 'plot_timing.pdf'
set encoding utf8

# Color definitions
set colorsequence default

# Styles
set border linewidth 1.8
set style fill solid 1.00 noborder
set for [i=1:7] linetype i dashtype i

# Titles
set title noenhanced
set ylabel "Time [ms] " offset 1.1 font "Helvetica-Oblique,16"

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

#set key bmargin center horizontal Right noreverse noenhanced autotitle columnhead nobox
#set key invert samplen 4 spacing 1 width 0 height 0 
#set key autotitle columnheader
#set key outside below center horizontal
set key at 1,1.1e4 
set style increment default
set style histogram clustered gap 2 title textcolor lt -1 font ",18"  offset character 2, -2
set datafile missing '-'
set style data histograms
set xtics border in scale 1,0.5 mirror font ", 10" rotate by -45  autojustify
set xtics  norangelimit 
set xtics   ()
set xtic noenhanced
#set title "Algorithm Timings" 
#set xlabel "Algorithms" 
set xrange [ * : * ] noreverse writeback
set x2range [ * : * ] noreverse writeback
set yrange [ * : * ] noreverse writeback
set y2range [ * : * ] noreverse writeback
set zrange [ * : * ] noreverse writeback
set cbrange [ * : * ] noreverse writeback
set rrange [ * : * ] noreverse writeback
#set bmargin  12
set datafile separator ";"

# Plot
plot newhistogram "", "../stats/timings.csv" using "Count":xtic(1) t col, \
															  '' u "Freq (K=10)" t col, \
															  '' u "Freq (K=20)" t col, \
															  '' u "Freq (All)" t col, \
															  '' u "InverseIndex (50)" t col, \
															  '' u "InverseIndex (All)" t col, \
#