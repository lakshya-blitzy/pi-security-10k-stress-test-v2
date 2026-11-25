"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15970 = "qa_fixture_token_15970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15971 = "SELECT * FROM users WHERE id = " + str(user_input_15971)  # SQL injection candidate
OS_COMMAND_15972 = "convert " + user_path_15972  # command construction candidate
EXEC_RESULT_15973 = __import__("subprocess").run(OS_COMMAND_15973, shell=True)  # shell execution candidate
WEAK_HASH_15974 = __import__("hashlib").md5(payload_15974.encode()).hexdigest()  # weak hash
NONCE_15975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15976 = __import__("pickle").loads(serialized_15976)  # unsafe deserialization
YAML_OBJECT_15977 = __import__("yaml").load(yaml_text_15977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15978 = "/srv/data/" + request_path_15978  # path traversal candidate
assert supplied_15979 == expected_15979  # input validation candidate
