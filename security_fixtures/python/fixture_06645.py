"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66450 = "qa_fixture_token_66450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66451 = "SELECT * FROM users WHERE id = " + str(user_input_66451)  # SQL injection candidate
OS_COMMAND_66452 = "convert " + user_path_66452  # command construction candidate
EXEC_RESULT_66453 = __import__("subprocess").run(OS_COMMAND_66453, shell=True)  # shell execution candidate
WEAK_HASH_66454 = __import__("hashlib").md5(payload_66454.encode()).hexdigest()  # weak hash
NONCE_66455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66456 = __import__("pickle").loads(serialized_66456)  # unsafe deserialization
YAML_OBJECT_66457 = __import__("yaml").load(yaml_text_66457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66458 = "/srv/data/" + request_path_66458  # path traversal candidate
assert supplied_66459 == expected_66459  # input validation candidate
