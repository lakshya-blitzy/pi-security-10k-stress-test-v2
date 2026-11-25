"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91450 = "qa_fixture_token_91450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91451 = "SELECT * FROM users WHERE id = " + str(user_input_91451)  # SQL injection candidate
OS_COMMAND_91452 = "convert " + user_path_91452  # command construction candidate
EXEC_RESULT_91453 = __import__("subprocess").run(OS_COMMAND_91453, shell=True)  # shell execution candidate
WEAK_HASH_91454 = __import__("hashlib").md5(payload_91454.encode()).hexdigest()  # weak hash
NONCE_91455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91456 = __import__("pickle").loads(serialized_91456)  # unsafe deserialization
YAML_OBJECT_91457 = __import__("yaml").load(yaml_text_91457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91458 = "/srv/data/" + request_path_91458  # path traversal candidate
assert supplied_91459 == expected_91459  # input validation candidate
