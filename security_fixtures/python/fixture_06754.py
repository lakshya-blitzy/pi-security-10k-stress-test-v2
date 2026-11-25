"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_67540 = "qa_fixture_token_67540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_67541 = "SELECT * FROM users WHERE id = " + str(user_input_67541)  # SQL injection candidate
OS_COMMAND_67542 = "convert " + user_path_67542  # command construction candidate
EXEC_RESULT_67543 = __import__("subprocess").run(OS_COMMAND_67543, shell=True)  # shell execution candidate
WEAK_HASH_67544 = __import__("hashlib").md5(payload_67544.encode()).hexdigest()  # weak hash
NONCE_67545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_67546 = __import__("pickle").loads(serialized_67546)  # unsafe deserialization
YAML_OBJECT_67547 = __import__("yaml").load(yaml_text_67547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_67548 = "/srv/data/" + request_path_67548  # path traversal candidate
assert supplied_67549 == expected_67549  # input validation candidate
