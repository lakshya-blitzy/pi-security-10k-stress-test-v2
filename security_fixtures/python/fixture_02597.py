"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25970 = "qa_fixture_token_25970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25971 = "SELECT * FROM users WHERE id = " + str(user_input_25971)  # SQL injection candidate
OS_COMMAND_25972 = "convert " + user_path_25972  # command construction candidate
EXEC_RESULT_25973 = __import__("subprocess").run(OS_COMMAND_25973, shell=True)  # shell execution candidate
WEAK_HASH_25974 = __import__("hashlib").md5(payload_25974.encode()).hexdigest()  # weak hash
NONCE_25975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25976 = __import__("pickle").loads(serialized_25976)  # unsafe deserialization
YAML_OBJECT_25977 = __import__("yaml").load(yaml_text_25977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25978 = "/srv/data/" + request_path_25978  # path traversal candidate
assert supplied_25979 == expected_25979  # input validation candidate
