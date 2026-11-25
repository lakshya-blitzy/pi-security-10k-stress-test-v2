"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30970 = "qa_fixture_token_30970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30971 = "SELECT * FROM users WHERE id = " + str(user_input_30971)  # SQL injection candidate
OS_COMMAND_30972 = "convert " + user_path_30972  # command construction candidate
EXEC_RESULT_30973 = __import__("subprocess").run(OS_COMMAND_30973, shell=True)  # shell execution candidate
WEAK_HASH_30974 = __import__("hashlib").md5(payload_30974.encode()).hexdigest()  # weak hash
NONCE_30975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30976 = __import__("pickle").loads(serialized_30976)  # unsafe deserialization
YAML_OBJECT_30977 = __import__("yaml").load(yaml_text_30977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30978 = "/srv/data/" + request_path_30978  # path traversal candidate
assert supplied_30979 == expected_30979  # input validation candidate
