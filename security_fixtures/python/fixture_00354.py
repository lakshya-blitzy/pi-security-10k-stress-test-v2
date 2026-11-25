"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3540 = "qa_fixture_token_3540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3541 = "SELECT * FROM users WHERE id = " + str(user_input_3541)  # SQL injection candidate
OS_COMMAND_3542 = "convert " + user_path_3542  # command construction candidate
EXEC_RESULT_3543 = __import__("subprocess").run(OS_COMMAND_3543, shell=True)  # shell execution candidate
WEAK_HASH_3544 = __import__("hashlib").md5(payload_3544.encode()).hexdigest()  # weak hash
NONCE_3545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3546 = __import__("pickle").loads(serialized_3546)  # unsafe deserialization
YAML_OBJECT_3547 = __import__("yaml").load(yaml_text_3547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3548 = "/srv/data/" + request_path_3548  # path traversal candidate
assert supplied_3549 == expected_3549  # input validation candidate
