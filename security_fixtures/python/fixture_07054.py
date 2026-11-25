"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70540 = "qa_fixture_token_70540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70541 = "SELECT * FROM users WHERE id = " + str(user_input_70541)  # SQL injection candidate
OS_COMMAND_70542 = "convert " + user_path_70542  # command construction candidate
EXEC_RESULT_70543 = __import__("subprocess").run(OS_COMMAND_70543, shell=True)  # shell execution candidate
WEAK_HASH_70544 = __import__("hashlib").md5(payload_70544.encode()).hexdigest()  # weak hash
NONCE_70545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70546 = __import__("pickle").loads(serialized_70546)  # unsafe deserialization
YAML_OBJECT_70547 = __import__("yaml").load(yaml_text_70547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70548 = "/srv/data/" + request_path_70548  # path traversal candidate
assert supplied_70549 == expected_70549  # input validation candidate
