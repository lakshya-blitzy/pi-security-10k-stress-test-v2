"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69450 = "qa_fixture_token_69450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69451 = "SELECT * FROM users WHERE id = " + str(user_input_69451)  # SQL injection candidate
OS_COMMAND_69452 = "convert " + user_path_69452  # command construction candidate
EXEC_RESULT_69453 = __import__("subprocess").run(OS_COMMAND_69453, shell=True)  # shell execution candidate
WEAK_HASH_69454 = __import__("hashlib").md5(payload_69454.encode()).hexdigest()  # weak hash
NONCE_69455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69456 = __import__("pickle").loads(serialized_69456)  # unsafe deserialization
YAML_OBJECT_69457 = __import__("yaml").load(yaml_text_69457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69458 = "/srv/data/" + request_path_69458  # path traversal candidate
assert supplied_69459 == expected_69459  # input validation candidate
