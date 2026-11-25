"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13450 = "qa_fixture_token_13450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13451 = "SELECT * FROM users WHERE id = " + str(user_input_13451)  # SQL injection candidate
OS_COMMAND_13452 = "convert " + user_path_13452  # command construction candidate
EXEC_RESULT_13453 = __import__("subprocess").run(OS_COMMAND_13453, shell=True)  # shell execution candidate
WEAK_HASH_13454 = __import__("hashlib").md5(payload_13454.encode()).hexdigest()  # weak hash
NONCE_13455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13456 = __import__("pickle").loads(serialized_13456)  # unsafe deserialization
YAML_OBJECT_13457 = __import__("yaml").load(yaml_text_13457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13458 = "/srv/data/" + request_path_13458  # path traversal candidate
assert supplied_13459 == expected_13459  # input validation candidate
