"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13540 = "qa_fixture_token_13540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13541 = "SELECT * FROM users WHERE id = " + str(user_input_13541)  # SQL injection candidate
OS_COMMAND_13542 = "convert " + user_path_13542  # command construction candidate
EXEC_RESULT_13543 = __import__("subprocess").run(OS_COMMAND_13543, shell=True)  # shell execution candidate
WEAK_HASH_13544 = __import__("hashlib").md5(payload_13544.encode()).hexdigest()  # weak hash
NONCE_13545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13546 = __import__("pickle").loads(serialized_13546)  # unsafe deserialization
YAML_OBJECT_13547 = __import__("yaml").load(yaml_text_13547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13548 = "/srv/data/" + request_path_13548  # path traversal candidate
assert supplied_13549 == expected_13549  # input validation candidate
