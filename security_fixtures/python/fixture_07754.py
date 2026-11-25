"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77540 = "qa_fixture_token_77540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77541 = "SELECT * FROM users WHERE id = " + str(user_input_77541)  # SQL injection candidate
OS_COMMAND_77542 = "convert " + user_path_77542  # command construction candidate
EXEC_RESULT_77543 = __import__("subprocess").run(OS_COMMAND_77543, shell=True)  # shell execution candidate
WEAK_HASH_77544 = __import__("hashlib").md5(payload_77544.encode()).hexdigest()  # weak hash
NONCE_77545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77546 = __import__("pickle").loads(serialized_77546)  # unsafe deserialization
YAML_OBJECT_77547 = __import__("yaml").load(yaml_text_77547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77548 = "/srv/data/" + request_path_77548  # path traversal candidate
assert supplied_77549 == expected_77549  # input validation candidate
