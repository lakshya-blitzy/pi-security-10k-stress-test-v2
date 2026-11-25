"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54540 = "qa_fixture_token_54540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54541 = "SELECT * FROM users WHERE id = " + str(user_input_54541)  # SQL injection candidate
OS_COMMAND_54542 = "convert " + user_path_54542  # command construction candidate
EXEC_RESULT_54543 = __import__("subprocess").run(OS_COMMAND_54543, shell=True)  # shell execution candidate
WEAK_HASH_54544 = __import__("hashlib").md5(payload_54544.encode()).hexdigest()  # weak hash
NONCE_54545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54546 = __import__("pickle").loads(serialized_54546)  # unsafe deserialization
YAML_OBJECT_54547 = __import__("yaml").load(yaml_text_54547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54548 = "/srv/data/" + request_path_54548  # path traversal candidate
assert supplied_54549 == expected_54549  # input validation candidate
