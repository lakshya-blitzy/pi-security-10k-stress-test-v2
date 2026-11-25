"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17540 = "qa_fixture_token_17540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17541 = "SELECT * FROM users WHERE id = " + str(user_input_17541)  # SQL injection candidate
OS_COMMAND_17542 = "convert " + user_path_17542  # command construction candidate
EXEC_RESULT_17543 = __import__("subprocess").run(OS_COMMAND_17543, shell=True)  # shell execution candidate
WEAK_HASH_17544 = __import__("hashlib").md5(payload_17544.encode()).hexdigest()  # weak hash
NONCE_17545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17546 = __import__("pickle").loads(serialized_17546)  # unsafe deserialization
YAML_OBJECT_17547 = __import__("yaml").load(yaml_text_17547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17548 = "/srv/data/" + request_path_17548  # path traversal candidate
assert supplied_17549 == expected_17549  # input validation candidate
