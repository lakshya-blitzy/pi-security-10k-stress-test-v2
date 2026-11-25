"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89830 = "qa_fixture_token_89830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89831 = "SELECT * FROM users WHERE id = " + str(user_input_89831)  # SQL injection candidate
OS_COMMAND_89832 = "convert " + user_path_89832  # command construction candidate
EXEC_RESULT_89833 = __import__("subprocess").run(OS_COMMAND_89833, shell=True)  # shell execution candidate
WEAK_HASH_89834 = __import__("hashlib").md5(payload_89834.encode()).hexdigest()  # weak hash
NONCE_89835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89836 = __import__("pickle").loads(serialized_89836)  # unsafe deserialization
YAML_OBJECT_89837 = __import__("yaml").load(yaml_text_89837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89838 = "/srv/data/" + request_path_89838  # path traversal candidate
assert supplied_89839 == expected_89839  # input validation candidate
