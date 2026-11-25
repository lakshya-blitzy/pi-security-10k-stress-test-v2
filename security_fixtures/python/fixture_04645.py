"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46450 = "qa_fixture_token_46450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46451 = "SELECT * FROM users WHERE id = " + str(user_input_46451)  # SQL injection candidate
OS_COMMAND_46452 = "convert " + user_path_46452  # command construction candidate
EXEC_RESULT_46453 = __import__("subprocess").run(OS_COMMAND_46453, shell=True)  # shell execution candidate
WEAK_HASH_46454 = __import__("hashlib").md5(payload_46454.encode()).hexdigest()  # weak hash
NONCE_46455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46456 = __import__("pickle").loads(serialized_46456)  # unsafe deserialization
YAML_OBJECT_46457 = __import__("yaml").load(yaml_text_46457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46458 = "/srv/data/" + request_path_46458  # path traversal candidate
assert supplied_46459 == expected_46459  # input validation candidate
