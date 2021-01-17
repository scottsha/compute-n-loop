#K8
for m in range(1,302):
    name = 'K8_' + str(m)
    file = open('mqsub/1-3_loops/templates/template_' + name, 'w')
    file.write('/nv/hp24/esabo3/scratch/six_loop/nzdata/nz_exact_' + name + '.sobj\n')
    file.close()

#8 (plain)
for m in range(1,22):
    name = '8_' + str(m)
    file = open('mqsub/1-3_loops/templates/template_' + name, 'w')
    file.write('/nv/hp24/esabo3/scratch/six_loop/nzdata/nz_exact_' + name + '.sobj\n')
    file.close()

#8a
for m in range(1,19):
    name = 'K8a_' + str(m)
    file = open('mqsub/1-3_loops/templates/template_' + name, 'w')
    file.write('/nv/hp24/esabo3/scratch/six_loop/nzdata/nz_exact_' + name + '.sobj\n')
    file.close()

#8n
for m in range(1,3):
    name = 'K8n_' + str(m)
    file = open('mqsub/1-3_loops/templates/template_' + name, 'w')
    file.write('/nv/hp24/esabo3/scratch/six_loop/nzdata/nz_exact_' + name + '.sobj\n')
    file.close()

#9 (plain)
for m in range(2,50):
    if m != 40:
        name = '9_' + str(m)
        file = open('mqsub/1-3_loops/templates/template_' + name, 'w')
        file.write('/nv/hp24/esabo3/scratch/six_loop/nzdata/nz_exact_' + name + '.sobj\n')
        file.close()

#K9a
for m in range(2,50):
    if m not in [1, 5, 6, 11, 28, 29, 30, 31, 32, 37]:
        name = 'K9a_' + str(m)
        file = open('mqsub/1-3_loops/templates/template_' + name, 'w')
        file.write('/nv/hp24/esabo3/scratch/six_loop/nzdata/nz_exact_' + name + '.sobj\n')
        file.close()

#K9n
for m in range(1,10):
    name = 'K9n_' + str(m)
    file = open('mqsub/1-3_loops/templates/template_' + name, 'w')
    file.write('/nv/hp24/esabo3/scratch/six_loop/nzdata/nz_exact_' + name + '.sobj\n')
    file.close()
