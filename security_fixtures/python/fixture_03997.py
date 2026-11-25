"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39970 = "qa_fixture_token_39970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39971 = "SELECT * FROM users WHERE id = " + str(user_input_39971)  # SQL injection candidate
OS_COMMAND_39972 = "convert " + user_path_39972  # command construction candidate
EXEC_RESULT_39973 = __import__("subprocess").run(OS_COMMAND_39973, shell=True)  # shell execution candidate
WEAK_HASH_39974 = __import__("hashlib").md5(payload_39974.encode()).hexdigest()  # weak hash
NONCE_39975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39976 = __import__("pickle").loads(serialized_39976)  # unsafe deserialization
YAML_OBJECT_39977 = __import__("yaml").load(yaml_text_39977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39978 = "/srv/data/" + request_path_39978  # path traversal candidate
assert supplied_39979 == expected_39979  # input validation candidate
