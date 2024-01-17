Great! It looks like you've outlined the basic steps for users to get started with your Nessus Compliance Parser. Now, let's update the README file to provide more detailed instructions on how users can use your project. Below is an updated version of your README:

```markdown
# Nessus Compliance Parser

Nessus Compliance Parser is a Python script that converts CSV files to JSON and processes the JSON data to filter and generate a final CSV file with combined and unique data.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/exrienz/Nessus-Compliance-Parser.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Nessus-Compliance-Parser
   ```

3. Copy all raw default exported CSV files to the same folder.

4. Run the script:

   ```bash
   python nessus_compliance_parser.py
   ```

5. Follow the on-screen prompts:

   - Enter the final CSV filename (without extension).
   - The script will process the CSV files, convert them to JSON, filter the data, and generate a final CSV file.

6. Find the combined and unique data in the specified final CSV file.

## Example

Assuming you have a CSV file named `example.csv` in the project directory, and you want to generate a final CSV file named `output.csv`, here's an example:

```bash
python nessus_compliance_parser.py
```

Enter `output` when prompted for the final CSV filename.

## Contributing

Contributions are welcome! If you have ideas for improvements, bug reports, or want to contribute new features, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m 'Add your feature'`.
4. Push the branch to your fork: `git push origin feature/your-feature`.
5. Create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
```

Feel free to customize this template further based on your specific project details or any additional information you want to provide to users.
