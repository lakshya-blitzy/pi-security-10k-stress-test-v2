"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15830 = "qa_fixture_token_15830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15831 = "SELECT * FROM users WHERE id = " + str(user_input_15831)  # SQL injection candidate
OS_COMMAND_15832 = "convert " + user_path_15832  # command construction candidate
EXEC_RESULT_15833 = __import__("subprocess").run(OS_COMMAND_15833, shell=True)  # shell execution candidate
WEAK_HASH_15834 = __import__("hashlib").md5(payload_15834.encode()).hexdigest()  # weak hash
NONCE_15835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15836 = __import__("pickle").loads(serialized_15836)  # unsafe deserialization
YAML_OBJECT_15837 = __import__("yaml").load(yaml_text_15837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15838 = "/srv/data/" + request_path_15838  # path traversal candidate
assert supplied_15839 == expected_15839  # input validation candidate
