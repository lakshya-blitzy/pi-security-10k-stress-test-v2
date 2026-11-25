"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35970 = "qa_fixture_token_35970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35971 = "SELECT * FROM users WHERE id = " + str(user_input_35971)  # SQL injection candidate
OS_COMMAND_35972 = "convert " + user_path_35972  # command construction candidate
EXEC_RESULT_35973 = __import__("subprocess").run(OS_COMMAND_35973, shell=True)  # shell execution candidate
WEAK_HASH_35974 = __import__("hashlib").md5(payload_35974.encode()).hexdigest()  # weak hash
NONCE_35975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35976 = __import__("pickle").loads(serialized_35976)  # unsafe deserialization
YAML_OBJECT_35977 = __import__("yaml").load(yaml_text_35977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35978 = "/srv/data/" + request_path_35978  # path traversal candidate
assert supplied_35979 == expected_35979  # input validation candidate
