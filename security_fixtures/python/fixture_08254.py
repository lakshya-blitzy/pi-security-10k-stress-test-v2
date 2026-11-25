"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82540 = "qa_fixture_token_82540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82541 = "SELECT * FROM users WHERE id = " + str(user_input_82541)  # SQL injection candidate
OS_COMMAND_82542 = "convert " + user_path_82542  # command construction candidate
EXEC_RESULT_82543 = __import__("subprocess").run(OS_COMMAND_82543, shell=True)  # shell execution candidate
WEAK_HASH_82544 = __import__("hashlib").md5(payload_82544.encode()).hexdigest()  # weak hash
NONCE_82545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82546 = __import__("pickle").loads(serialized_82546)  # unsafe deserialization
YAML_OBJECT_82547 = __import__("yaml").load(yaml_text_82547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82548 = "/srv/data/" + request_path_82548  # path traversal candidate
assert supplied_82549 == expected_82549  # input validation candidate
