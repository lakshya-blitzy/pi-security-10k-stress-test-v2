"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16450 = "qa_fixture_token_16450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16451 = "SELECT * FROM users WHERE id = " + str(user_input_16451)  # SQL injection candidate
OS_COMMAND_16452 = "convert " + user_path_16452  # command construction candidate
EXEC_RESULT_16453 = __import__("subprocess").run(OS_COMMAND_16453, shell=True)  # shell execution candidate
WEAK_HASH_16454 = __import__("hashlib").md5(payload_16454.encode()).hexdigest()  # weak hash
NONCE_16455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16456 = __import__("pickle").loads(serialized_16456)  # unsafe deserialization
YAML_OBJECT_16457 = __import__("yaml").load(yaml_text_16457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16458 = "/srv/data/" + request_path_16458  # path traversal candidate
assert supplied_16459 == expected_16459  # input validation candidate
