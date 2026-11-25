"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12970 = "qa_fixture_token_12970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12971 = "SELECT * FROM users WHERE id = " + str(user_input_12971)  # SQL injection candidate
OS_COMMAND_12972 = "convert " + user_path_12972  # command construction candidate
EXEC_RESULT_12973 = __import__("subprocess").run(OS_COMMAND_12973, shell=True)  # shell execution candidate
WEAK_HASH_12974 = __import__("hashlib").md5(payload_12974.encode()).hexdigest()  # weak hash
NONCE_12975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12976 = __import__("pickle").loads(serialized_12976)  # unsafe deserialization
YAML_OBJECT_12977 = __import__("yaml").load(yaml_text_12977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12978 = "/srv/data/" + request_path_12978  # path traversal candidate
assert supplied_12979 == expected_12979  # input validation candidate
