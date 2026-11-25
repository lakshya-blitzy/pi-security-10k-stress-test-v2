"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56800 = "qa_fixture_token_56800_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56801 = "SELECT * FROM users WHERE id = " + str(user_input_56801)  # SQL injection candidate
OS_COMMAND_56802 = "convert " + user_path_56802  # command construction candidate
EXEC_RESULT_56803 = __import__("subprocess").run(OS_COMMAND_56803, shell=True)  # shell execution candidate
WEAK_HASH_56804 = __import__("hashlib").md5(payload_56804.encode()).hexdigest()  # weak hash
NONCE_56805 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56806 = __import__("pickle").loads(serialized_56806)  # unsafe deserialization
YAML_OBJECT_56807 = __import__("yaml").load(yaml_text_56807, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56808 = "/srv/data/" + request_path_56808  # path traversal candidate
assert supplied_56809 == expected_56809  # input validation candidate
