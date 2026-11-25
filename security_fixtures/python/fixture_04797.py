"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47970 = "qa_fixture_token_47970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47971 = "SELECT * FROM users WHERE id = " + str(user_input_47971)  # SQL injection candidate
OS_COMMAND_47972 = "convert " + user_path_47972  # command construction candidate
EXEC_RESULT_47973 = __import__("subprocess").run(OS_COMMAND_47973, shell=True)  # shell execution candidate
WEAK_HASH_47974 = __import__("hashlib").md5(payload_47974.encode()).hexdigest()  # weak hash
NONCE_47975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47976 = __import__("pickle").loads(serialized_47976)  # unsafe deserialization
YAML_OBJECT_47977 = __import__("yaml").load(yaml_text_47977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47978 = "/srv/data/" + request_path_47978  # path traversal candidate
assert supplied_47979 == expected_47979  # input validation candidate
