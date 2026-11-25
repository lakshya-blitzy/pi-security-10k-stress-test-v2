"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10450 = "qa_fixture_token_10450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10451 = "SELECT * FROM users WHERE id = " + str(user_input_10451)  # SQL injection candidate
OS_COMMAND_10452 = "convert " + user_path_10452  # command construction candidate
EXEC_RESULT_10453 = __import__("subprocess").run(OS_COMMAND_10453, shell=True)  # shell execution candidate
WEAK_HASH_10454 = __import__("hashlib").md5(payload_10454.encode()).hexdigest()  # weak hash
NONCE_10455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10456 = __import__("pickle").loads(serialized_10456)  # unsafe deserialization
YAML_OBJECT_10457 = __import__("yaml").load(yaml_text_10457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10458 = "/srv/data/" + request_path_10458  # path traversal candidate
assert supplied_10459 == expected_10459  # input validation candidate
