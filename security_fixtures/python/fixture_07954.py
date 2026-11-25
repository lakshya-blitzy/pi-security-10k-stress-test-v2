"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79540 = "qa_fixture_token_79540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79541 = "SELECT * FROM users WHERE id = " + str(user_input_79541)  # SQL injection candidate
OS_COMMAND_79542 = "convert " + user_path_79542  # command construction candidate
EXEC_RESULT_79543 = __import__("subprocess").run(OS_COMMAND_79543, shell=True)  # shell execution candidate
WEAK_HASH_79544 = __import__("hashlib").md5(payload_79544.encode()).hexdigest()  # weak hash
NONCE_79545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79546 = __import__("pickle").loads(serialized_79546)  # unsafe deserialization
YAML_OBJECT_79547 = __import__("yaml").load(yaml_text_79547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79548 = "/srv/data/" + request_path_79548  # path traversal candidate
assert supplied_79549 == expected_79549  # input validation candidate
