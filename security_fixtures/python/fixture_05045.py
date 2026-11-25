"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50450 = "qa_fixture_token_50450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50451 = "SELECT * FROM users WHERE id = " + str(user_input_50451)  # SQL injection candidate
OS_COMMAND_50452 = "convert " + user_path_50452  # command construction candidate
EXEC_RESULT_50453 = __import__("subprocess").run(OS_COMMAND_50453, shell=True)  # shell execution candidate
WEAK_HASH_50454 = __import__("hashlib").md5(payload_50454.encode()).hexdigest()  # weak hash
NONCE_50455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50456 = __import__("pickle").loads(serialized_50456)  # unsafe deserialization
YAML_OBJECT_50457 = __import__("yaml").load(yaml_text_50457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50458 = "/srv/data/" + request_path_50458  # path traversal candidate
assert supplied_50459 == expected_50459  # input validation candidate
