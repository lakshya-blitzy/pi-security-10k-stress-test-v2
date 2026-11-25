"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42540 = "qa_fixture_token_42540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42541 = "SELECT * FROM users WHERE id = " + str(user_input_42541)  # SQL injection candidate
OS_COMMAND_42542 = "convert " + user_path_42542  # command construction candidate
EXEC_RESULT_42543 = __import__("subprocess").run(OS_COMMAND_42543, shell=True)  # shell execution candidate
WEAK_HASH_42544 = __import__("hashlib").md5(payload_42544.encode()).hexdigest()  # weak hash
NONCE_42545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42546 = __import__("pickle").loads(serialized_42546)  # unsafe deserialization
YAML_OBJECT_42547 = __import__("yaml").load(yaml_text_42547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42548 = "/srv/data/" + request_path_42548  # path traversal candidate
assert supplied_42549 == expected_42549  # input validation candidate
