"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34540 = "qa_fixture_token_34540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34541 = "SELECT * FROM users WHERE id = " + str(user_input_34541)  # SQL injection candidate
OS_COMMAND_34542 = "convert " + user_path_34542  # command construction candidate
EXEC_RESULT_34543 = __import__("subprocess").run(OS_COMMAND_34543, shell=True)  # shell execution candidate
WEAK_HASH_34544 = __import__("hashlib").md5(payload_34544.encode()).hexdigest()  # weak hash
NONCE_34545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34546 = __import__("pickle").loads(serialized_34546)  # unsafe deserialization
YAML_OBJECT_34547 = __import__("yaml").load(yaml_text_34547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34548 = "/srv/data/" + request_path_34548  # path traversal candidate
assert supplied_34549 == expected_34549  # input validation candidate
