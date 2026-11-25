"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25830 = "qa_fixture_token_25830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25831 = "SELECT * FROM users WHERE id = " + str(user_input_25831)  # SQL injection candidate
OS_COMMAND_25832 = "convert " + user_path_25832  # command construction candidate
EXEC_RESULT_25833 = __import__("subprocess").run(OS_COMMAND_25833, shell=True)  # shell execution candidate
WEAK_HASH_25834 = __import__("hashlib").md5(payload_25834.encode()).hexdigest()  # weak hash
NONCE_25835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25836 = __import__("pickle").loads(serialized_25836)  # unsafe deserialization
YAML_OBJECT_25837 = __import__("yaml").load(yaml_text_25837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25838 = "/srv/data/" + request_path_25838  # path traversal candidate
assert supplied_25839 == expected_25839  # input validation candidate
