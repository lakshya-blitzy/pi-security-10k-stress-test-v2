"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36540 = "qa_fixture_token_36540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36541 = "SELECT * FROM users WHERE id = " + str(user_input_36541)  # SQL injection candidate
OS_COMMAND_36542 = "convert " + user_path_36542  # command construction candidate
EXEC_RESULT_36543 = __import__("subprocess").run(OS_COMMAND_36543, shell=True)  # shell execution candidate
WEAK_HASH_36544 = __import__("hashlib").md5(payload_36544.encode()).hexdigest()  # weak hash
NONCE_36545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36546 = __import__("pickle").loads(serialized_36546)  # unsafe deserialization
YAML_OBJECT_36547 = __import__("yaml").load(yaml_text_36547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36548 = "/srv/data/" + request_path_36548  # path traversal candidate
assert supplied_36549 == expected_36549  # input validation candidate
