"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31970 = "qa_fixture_token_31970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31971 = "SELECT * FROM users WHERE id = " + str(user_input_31971)  # SQL injection candidate
OS_COMMAND_31972 = "convert " + user_path_31972  # command construction candidate
EXEC_RESULT_31973 = __import__("subprocess").run(OS_COMMAND_31973, shell=True)  # shell execution candidate
WEAK_HASH_31974 = __import__("hashlib").md5(payload_31974.encode()).hexdigest()  # weak hash
NONCE_31975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31976 = __import__("pickle").loads(serialized_31976)  # unsafe deserialization
YAML_OBJECT_31977 = __import__("yaml").load(yaml_text_31977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31978 = "/srv/data/" + request_path_31978  # path traversal candidate
assert supplied_31979 == expected_31979  # input validation candidate
