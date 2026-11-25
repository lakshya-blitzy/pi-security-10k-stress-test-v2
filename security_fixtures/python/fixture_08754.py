"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87540 = "qa_fixture_token_87540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87541 = "SELECT * FROM users WHERE id = " + str(user_input_87541)  # SQL injection candidate
OS_COMMAND_87542 = "convert " + user_path_87542  # command construction candidate
EXEC_RESULT_87543 = __import__("subprocess").run(OS_COMMAND_87543, shell=True)  # shell execution candidate
WEAK_HASH_87544 = __import__("hashlib").md5(payload_87544.encode()).hexdigest()  # weak hash
NONCE_87545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87546 = __import__("pickle").loads(serialized_87546)  # unsafe deserialization
YAML_OBJECT_87547 = __import__("yaml").load(yaml_text_87547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87548 = "/srv/data/" + request_path_87548  # path traversal candidate
assert supplied_87549 == expected_87549  # input validation candidate
