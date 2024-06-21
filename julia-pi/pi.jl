# Import the necessary packages
using Random

# Get the number of points from the environment variable or use a default value
num_points = parse(Int, get(ENV, "NUM_POINTS", "100000"))

# Define a function to approximate pi
function approximate_pi(num_points)
    # Initialize the counters
    inside_circle = 0
    total_points = 0

    # Set the random seed
    Random.seed!(123)

    # Generate random points and count the number of points inside the circle
    for _ in 1:num_points
        x = rand()
        y = rand()
        if x^2 + y^2 <= 1
            inside_circle += 1
        end
        total_points += 1
    end

    # Compute the approximation of pi
    pi_approx = 4 * inside_circle / total_points

    # Return the approximation
    return pi_approx
end

# Call the function with the specified number of points
pi_approx = approximate_pi(num_points)

# Print the result
println(pi_approx)
