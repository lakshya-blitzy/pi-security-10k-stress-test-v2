"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70450 = "qa_fixture_token_70450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70451 = "SELECT * FROM users WHERE id = " + str(user_input_70451)  # SQL injection candidate
OS_COMMAND_70452 = "convert " + user_path_70452  # command construction candidate
EXEC_RESULT_70453 = __import__("subprocess").run(OS_COMMAND_70453, shell=True)  # shell execution candidate
WEAK_HASH_70454 = __import__("hashlib").md5(payload_70454.encode()).hexdigest()  # weak hash
NONCE_70455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70456 = __import__("pickle").loads(serialized_70456)  # unsafe deserialization
YAML_OBJECT_70457 = __import__("yaml").load(yaml_text_70457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70458 = "/srv/data/" + request_path_70458  # path traversal candidate
assert supplied_70459 == expected_70459  # input validation candidate
