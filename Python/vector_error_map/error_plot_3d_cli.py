import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import argparse # Import argparse

def plot_3d_vector_error_map(csv_filepath):
    """
    Reads 3D data from a CSV file (specified by path) and plots a 3D vector error map.

    The CSV file should contain 'x', 'y', 'z', 
    'x_error', 'y_error', and 'z_error' columns.
    (x,y,z) are the positions of dots (arrow tails).
    (x_error, y_error, z_error) are the components of the arrows.

    Args:
        csv_filepath (str): The path to the CSV file.
    """
    try:
        # Read the data from the CSV file
        data = pd.read_csv(csv_filepath)

        # Ensure the required columns exist
        required_columns = ['x', 'y', 'z', 'x_error', 'y_error', 'z_error']
        if not all(col in data.columns for col in required_columns):
            print(f"Error: CSV file must contain the columns: {', '.join(required_columns)}")
            print(f"Found columns: {data.columns.tolist()}")
            return

        x = data['x']
        y = data['y']
        z = data['z']
        x_error = data['x_error']
        y_error = data['y_error']
        z_error = data['z_error']

        # Create the 3D plot
        fig = plt.figure(figsize=(12, 10))
        ax = fig.add_subplot(111, projection='3d')
        
        ax.scatter(x, y, z, color='blue', s=10, label='Data Points (x,y,z)')
        ax.quiver(x, y, z, x_error, y_error, z_error, 
                  length=0.1, 
                  normalize=False, 
                  color='red', alpha=0.7, label='Error Vectors (dx, dy, dz)',
                  arrow_length_ratio=0.3)

        ax.set_xlabel("X coordinate")
        ax.set_ylabel("Y coordinate")
        ax.set_zlabel("Z coordinate")
        ax.set_title("3D Vector Error Map")
        
        # Basic dynamic limits
        ax.set_xlim([(x + x_error).min() - 0.1 if not x.empty else 0, (x + x_error).max() + 0.1 if not x.empty else 1])
        ax.set_ylim([(y + y_error).min() - 0.1 if not y.empty else 0, (y + y_error).max() + 0.1 if not y.empty else 1])
        ax.set_zlim([(z + z_error).min() - 0.1 if not z.empty else 0, (z + z_error).max() + 0.1 if not z.empty else 1])

        ax.legend()
        plt.show()

    except FileNotFoundError:
        print(f"Error: The file '{csv_filepath}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file '{csv_filepath}' is empty.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a 3D vector error map from a CSV file.")
    parser.add_argument("csv_filepath", help="Path to the input CSV file containing x, y, z, x_error, y_error, z_error columns.")
    
    # Parse arguments
    args = parser.parse_args()
    
    # Call the plotting function with the provided filepath
    plot_3d_vector_error_map(args.csv_filepath)