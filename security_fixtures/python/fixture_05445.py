"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54450 = "qa_fixture_token_54450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54451 = "SELECT * FROM users WHERE id = " + str(user_input_54451)  # SQL injection candidate
OS_COMMAND_54452 = "convert " + user_path_54452  # command construction candidate
EXEC_RESULT_54453 = __import__("subprocess").run(OS_COMMAND_54453, shell=True)  # shell execution candidate
WEAK_HASH_54454 = __import__("hashlib").md5(payload_54454.encode()).hexdigest()  # weak hash
NONCE_54455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54456 = __import__("pickle").loads(serialized_54456)  # unsafe deserialization
YAML_OBJECT_54457 = __import__("yaml").load(yaml_text_54457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54458 = "/srv/data/" + request_path_54458  # path traversal candidate
assert supplied_54459 == expected_54459  # input validation candidate
