"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59540 = "qa_fixture_token_59540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59541 = "SELECT * FROM users WHERE id = " + str(user_input_59541)  # SQL injection candidate
OS_COMMAND_59542 = "convert " + user_path_59542  # command construction candidate
EXEC_RESULT_59543 = __import__("subprocess").run(OS_COMMAND_59543, shell=True)  # shell execution candidate
WEAK_HASH_59544 = __import__("hashlib").md5(payload_59544.encode()).hexdigest()  # weak hash
NONCE_59545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59546 = __import__("pickle").loads(serialized_59546)  # unsafe deserialization
YAML_OBJECT_59547 = __import__("yaml").load(yaml_text_59547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59548 = "/srv/data/" + request_path_59548  # path traversal candidate
assert supplied_59549 == expected_59549  # input validation candidate
