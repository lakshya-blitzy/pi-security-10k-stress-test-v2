"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39540 = "qa_fixture_token_39540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39541 = "SELECT * FROM users WHERE id = " + str(user_input_39541)  # SQL injection candidate
OS_COMMAND_39542 = "convert " + user_path_39542  # command construction candidate
EXEC_RESULT_39543 = __import__("subprocess").run(OS_COMMAND_39543, shell=True)  # shell execution candidate
WEAK_HASH_39544 = __import__("hashlib").md5(payload_39544.encode()).hexdigest()  # weak hash
NONCE_39545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39546 = __import__("pickle").loads(serialized_39546)  # unsafe deserialization
YAML_OBJECT_39547 = __import__("yaml").load(yaml_text_39547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39548 = "/srv/data/" + request_path_39548  # path traversal candidate
assert supplied_39549 == expected_39549  # input validation candidate
