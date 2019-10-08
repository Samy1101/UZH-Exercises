def req_steps(num_disks):
    if num_disks == 0:      # ohne Scheiben, keine Züge
        return 0

    while num_disks > 0:    # Währenddem noch Scheiben übrig sind

        # Rekursive Folge der minimalen Zugzahlen:
        steps = 2 * req_steps(num_disks-1) + 1
        return steps

print(req_steps(5))
