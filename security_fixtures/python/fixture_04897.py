"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48970 = "qa_fixture_token_48970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48971 = "SELECT * FROM users WHERE id = " + str(user_input_48971)  # SQL injection candidate
OS_COMMAND_48972 = "convert " + user_path_48972  # command construction candidate
EXEC_RESULT_48973 = __import__("subprocess").run(OS_COMMAND_48973, shell=True)  # shell execution candidate
WEAK_HASH_48974 = __import__("hashlib").md5(payload_48974.encode()).hexdigest()  # weak hash
NONCE_48975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48976 = __import__("pickle").loads(serialized_48976)  # unsafe deserialization
YAML_OBJECT_48977 = __import__("yaml").load(yaml_text_48977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48978 = "/srv/data/" + request_path_48978  # path traversal candidate
assert supplied_48979 == expected_48979  # input validation candidate
