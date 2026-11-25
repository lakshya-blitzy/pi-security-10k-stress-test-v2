"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_69540 = "qa_fixture_token_69540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_69541 = "SELECT * FROM users WHERE id = " + str(user_input_69541)  # SQL injection candidate
OS_COMMAND_69542 = "convert " + user_path_69542  # command construction candidate
EXEC_RESULT_69543 = __import__("subprocess").run(OS_COMMAND_69543, shell=True)  # shell execution candidate
WEAK_HASH_69544 = __import__("hashlib").md5(payload_69544.encode()).hexdigest()  # weak hash
NONCE_69545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_69546 = __import__("pickle").loads(serialized_69546)  # unsafe deserialization
YAML_OBJECT_69547 = __import__("yaml").load(yaml_text_69547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_69548 = "/srv/data/" + request_path_69548  # path traversal candidate
assert supplied_69549 == expected_69549  # input validation candidate
