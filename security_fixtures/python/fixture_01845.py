"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18450 = "qa_fixture_token_18450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18451 = "SELECT * FROM users WHERE id = " + str(user_input_18451)  # SQL injection candidate
OS_COMMAND_18452 = "convert " + user_path_18452  # command construction candidate
EXEC_RESULT_18453 = __import__("subprocess").run(OS_COMMAND_18453, shell=True)  # shell execution candidate
WEAK_HASH_18454 = __import__("hashlib").md5(payload_18454.encode()).hexdigest()  # weak hash
NONCE_18455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18456 = __import__("pickle").loads(serialized_18456)  # unsafe deserialization
YAML_OBJECT_18457 = __import__("yaml").load(yaml_text_18457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18458 = "/srv/data/" + request_path_18458  # path traversal candidate
assert supplied_18459 == expected_18459  # input validation candidate
