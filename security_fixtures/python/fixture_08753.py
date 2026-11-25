"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87530 = "qa_fixture_token_87530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87531 = "SELECT * FROM users WHERE id = " + str(user_input_87531)  # SQL injection candidate
OS_COMMAND_87532 = "convert " + user_path_87532  # command construction candidate
EXEC_RESULT_87533 = __import__("subprocess").run(OS_COMMAND_87533, shell=True)  # shell execution candidate
WEAK_HASH_87534 = __import__("hashlib").md5(payload_87534.encode()).hexdigest()  # weak hash
NONCE_87535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87536 = __import__("pickle").loads(serialized_87536)  # unsafe deserialization
YAML_OBJECT_87537 = __import__("yaml").load(yaml_text_87537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87538 = "/srv/data/" + request_path_87538  # path traversal candidate
assert supplied_87539 == expected_87539  # input validation candidate
