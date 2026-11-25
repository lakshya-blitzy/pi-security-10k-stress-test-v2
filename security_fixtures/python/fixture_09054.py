"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90540 = "qa_fixture_token_90540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90541 = "SELECT * FROM users WHERE id = " + str(user_input_90541)  # SQL injection candidate
OS_COMMAND_90542 = "convert " + user_path_90542  # command construction candidate
EXEC_RESULT_90543 = __import__("subprocess").run(OS_COMMAND_90543, shell=True)  # shell execution candidate
WEAK_HASH_90544 = __import__("hashlib").md5(payload_90544.encode()).hexdigest()  # weak hash
NONCE_90545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90546 = __import__("pickle").loads(serialized_90546)  # unsafe deserialization
YAML_OBJECT_90547 = __import__("yaml").load(yaml_text_90547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90548 = "/srv/data/" + request_path_90548  # path traversal candidate
assert supplied_90549 == expected_90549  # input validation candidate
