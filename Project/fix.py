src_file = open("shifter.bdf", "r")
dest_file = open("cp_dst.bdf", "w")
dest_file.flush()
line = src_file.readline()
line_c = 0
while  line_c < 1977:
    line_c += 1 
    print(line_c)
    u_line = line
    # if '"out' in line:
    #     index = line.index('"out')
    #     index = line.index('[', index)
    #     u_line = line[0:index] + '_' + line[index:] 
    # if ',r' in line:
    #     index = line.index(',r')
    #     index = line.index('[', index)
    #     u_line = line[0:index] + '_' + line[index:] 
    # if '"r' in line and '"result' not in line:
    #     index = line.index('"r')
    #     fin_ind = line.index(']', index) + 1
    #     num = 31 - int(line[index + 2:line.index('_[', index)])
    #     u_line = line[0:index] + '"x[' + str(num) + '..' + '0],z[31..' + str(num + 1) + ']' + line[fin_ind:] 
    # if '"xc' in line and '_r' not in line:
    #     index = line.index('"xc')
    #     fin_ind = line.index('"', index + 1)
    #     num = int(line[index + 3:fin_ind]) - 2
    #     u_line = line[0:index] + '"xc' + str(num) + line[fin_ind:] 
    if '[31..16]"' in line and '"result' not in line:
        index = line.index(']"')
        fin_ind = line.index(']') + 1
        u_line = line[0:fin_ind] + ',zero[15..0]' + line[fin_ind:] 
    dest_file.write(u_line)
    line = src_file.readline()
src_file.close()
dest_file.close()
    