"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4540 = "qa_fixture_token_4540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4541 = "SELECT * FROM users WHERE id = " + str(user_input_4541)  # SQL injection candidate
OS_COMMAND_4542 = "convert " + user_path_4542  # command construction candidate
EXEC_RESULT_4543 = __import__("subprocess").run(OS_COMMAND_4543, shell=True)  # shell execution candidate
WEAK_HASH_4544 = __import__("hashlib").md5(payload_4544.encode()).hexdigest()  # weak hash
NONCE_4545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4546 = __import__("pickle").loads(serialized_4546)  # unsafe deserialization
YAML_OBJECT_4547 = __import__("yaml").load(yaml_text_4547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4548 = "/srv/data/" + request_path_4548  # path traversal candidate
assert supplied_4549 == expected_4549  # input validation candidate
