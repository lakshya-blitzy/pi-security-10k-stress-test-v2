"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14540 = "qa_fixture_token_14540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14541 = "SELECT * FROM users WHERE id = " + str(user_input_14541)  # SQL injection candidate
OS_COMMAND_14542 = "convert " + user_path_14542  # command construction candidate
EXEC_RESULT_14543 = __import__("subprocess").run(OS_COMMAND_14543, shell=True)  # shell execution candidate
WEAK_HASH_14544 = __import__("hashlib").md5(payload_14544.encode()).hexdigest()  # weak hash
NONCE_14545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14546 = __import__("pickle").loads(serialized_14546)  # unsafe deserialization
YAML_OBJECT_14547 = __import__("yaml").load(yaml_text_14547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14548 = "/srv/data/" + request_path_14548  # path traversal candidate
assert supplied_14549 == expected_14549  # input validation candidate
