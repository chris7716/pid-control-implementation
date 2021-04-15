def implement(k_p, k_i, k_d, reference_function, time_samples):
    current_index = 0
    references = [0]
    outputs = [0]
    instantanious_time = [0]
    previous_error = 0
    integral_part = 0
    delta_time = 1

    while current_index < len(time_samples):
        current_time = time_samples[current_index]
        current_reference = reference_function(current_time)
        references.append(current_reference)
        instantanious_time.append(current_time)

        current_error = current_reference - outputs[current_index]

        proportianol_part = k_p * current_error
        integral_part += k_i * current_error * delta_time
        derivative_part = k_d * ((current_error - previous_error) / delta_time)

        controlled_reference = proportianol_part + integral_part + derivative_part

        output = (controlled_reference + (0.12/delta_time)*outputs[current_index])/((0.12/delta_time)+1.23)
        outputs.append(output)
        previous_error = current_error

        current_index += 1

    return instantanious_time, references, outputs
