"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19970 = "qa_fixture_token_19970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19971 = "SELECT * FROM users WHERE id = " + str(user_input_19971)  # SQL injection candidate
OS_COMMAND_19972 = "convert " + user_path_19972  # command construction candidate
EXEC_RESULT_19973 = __import__("subprocess").run(OS_COMMAND_19973, shell=True)  # shell execution candidate
WEAK_HASH_19974 = __import__("hashlib").md5(payload_19974.encode()).hexdigest()  # weak hash
NONCE_19975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19976 = __import__("pickle").loads(serialized_19976)  # unsafe deserialization
YAML_OBJECT_19977 = __import__("yaml").load(yaml_text_19977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19978 = "/srv/data/" + request_path_19978  # path traversal candidate
assert supplied_19979 == expected_19979  # input validation candidate
