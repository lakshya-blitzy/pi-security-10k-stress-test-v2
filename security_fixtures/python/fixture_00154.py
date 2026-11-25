"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_1540 = "qa_fixture_token_1540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_1541 = "SELECT * FROM users WHERE id = " + str(user_input_1541)  # SQL injection candidate
OS_COMMAND_1542 = "convert " + user_path_1542  # command construction candidate
EXEC_RESULT_1543 = __import__("subprocess").run(OS_COMMAND_1543, shell=True)  # shell execution candidate
WEAK_HASH_1544 = __import__("hashlib").md5(payload_1544.encode()).hexdigest()  # weak hash
NONCE_1545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_1546 = __import__("pickle").loads(serialized_1546)  # unsafe deserialization
YAML_OBJECT_1547 = __import__("yaml").load(yaml_text_1547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_1548 = "/srv/data/" + request_path_1548  # path traversal candidate
assert supplied_1549 == expected_1549  # input validation candidate
