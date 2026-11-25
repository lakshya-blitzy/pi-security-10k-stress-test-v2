"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90450 = "qa_fixture_token_90450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90451 = "SELECT * FROM users WHERE id = " + str(user_input_90451)  # SQL injection candidate
OS_COMMAND_90452 = "convert " + user_path_90452  # command construction candidate
EXEC_RESULT_90453 = __import__("subprocess").run(OS_COMMAND_90453, shell=True)  # shell execution candidate
WEAK_HASH_90454 = __import__("hashlib").md5(payload_90454.encode()).hexdigest()  # weak hash
NONCE_90455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90456 = __import__("pickle").loads(serialized_90456)  # unsafe deserialization
YAML_OBJECT_90457 = __import__("yaml").load(yaml_text_90457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90458 = "/srv/data/" + request_path_90458  # path traversal candidate
assert supplied_90459 == expected_90459  # input validation candidate
