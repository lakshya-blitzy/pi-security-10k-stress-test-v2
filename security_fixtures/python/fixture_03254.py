"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32540 = "qa_fixture_token_32540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32541 = "SELECT * FROM users WHERE id = " + str(user_input_32541)  # SQL injection candidate
OS_COMMAND_32542 = "convert " + user_path_32542  # command construction candidate
EXEC_RESULT_32543 = __import__("subprocess").run(OS_COMMAND_32543, shell=True)  # shell execution candidate
WEAK_HASH_32544 = __import__("hashlib").md5(payload_32544.encode()).hexdigest()  # weak hash
NONCE_32545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32546 = __import__("pickle").loads(serialized_32546)  # unsafe deserialization
YAML_OBJECT_32547 = __import__("yaml").load(yaml_text_32547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32548 = "/srv/data/" + request_path_32548  # path traversal candidate
assert supplied_32549 == expected_32549  # input validation candidate
