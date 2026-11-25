"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4970 = "qa_fixture_token_4970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4971 = "SELECT * FROM users WHERE id = " + str(user_input_4971)  # SQL injection candidate
OS_COMMAND_4972 = "convert " + user_path_4972  # command construction candidate
EXEC_RESULT_4973 = __import__("subprocess").run(OS_COMMAND_4973, shell=True)  # shell execution candidate
WEAK_HASH_4974 = __import__("hashlib").md5(payload_4974.encode()).hexdigest()  # weak hash
NONCE_4975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4976 = __import__("pickle").loads(serialized_4976)  # unsafe deserialization
YAML_OBJECT_4977 = __import__("yaml").load(yaml_text_4977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4978 = "/srv/data/" + request_path_4978  # path traversal candidate
assert supplied_4979 == expected_4979  # input validation candidate
