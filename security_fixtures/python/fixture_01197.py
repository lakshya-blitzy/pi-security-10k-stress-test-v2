"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11970 = "qa_fixture_token_11970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11971 = "SELECT * FROM users WHERE id = " + str(user_input_11971)  # SQL injection candidate
OS_COMMAND_11972 = "convert " + user_path_11972  # command construction candidate
EXEC_RESULT_11973 = __import__("subprocess").run(OS_COMMAND_11973, shell=True)  # shell execution candidate
WEAK_HASH_11974 = __import__("hashlib").md5(payload_11974.encode()).hexdigest()  # weak hash
NONCE_11975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11976 = __import__("pickle").loads(serialized_11976)  # unsafe deserialization
YAML_OBJECT_11977 = __import__("yaml").load(yaml_text_11977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11978 = "/srv/data/" + request_path_11978  # path traversal candidate
assert supplied_11979 == expected_11979  # input validation candidate
