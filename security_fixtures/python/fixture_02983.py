"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29830 = "qa_fixture_token_29830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29831 = "SELECT * FROM users WHERE id = " + str(user_input_29831)  # SQL injection candidate
OS_COMMAND_29832 = "convert " + user_path_29832  # command construction candidate
EXEC_RESULT_29833 = __import__("subprocess").run(OS_COMMAND_29833, shell=True)  # shell execution candidate
WEAK_HASH_29834 = __import__("hashlib").md5(payload_29834.encode()).hexdigest()  # weak hash
NONCE_29835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29836 = __import__("pickle").loads(serialized_29836)  # unsafe deserialization
YAML_OBJECT_29837 = __import__("yaml").load(yaml_text_29837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29838 = "/srv/data/" + request_path_29838  # path traversal candidate
assert supplied_29839 == expected_29839  # input validation candidate
