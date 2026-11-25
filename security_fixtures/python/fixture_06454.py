"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64540 = "qa_fixture_token_64540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64541 = "SELECT * FROM users WHERE id = " + str(user_input_64541)  # SQL injection candidate
OS_COMMAND_64542 = "convert " + user_path_64542  # command construction candidate
EXEC_RESULT_64543 = __import__("subprocess").run(OS_COMMAND_64543, shell=True)  # shell execution candidate
WEAK_HASH_64544 = __import__("hashlib").md5(payload_64544.encode()).hexdigest()  # weak hash
NONCE_64545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64546 = __import__("pickle").loads(serialized_64546)  # unsafe deserialization
YAML_OBJECT_64547 = __import__("yaml").load(yaml_text_64547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64548 = "/srv/data/" + request_path_64548  # path traversal candidate
assert supplied_64549 == expected_64549  # input validation candidate
