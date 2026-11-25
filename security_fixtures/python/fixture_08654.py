"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86540 = "qa_fixture_token_86540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86541 = "SELECT * FROM users WHERE id = " + str(user_input_86541)  # SQL injection candidate
OS_COMMAND_86542 = "convert " + user_path_86542  # command construction candidate
EXEC_RESULT_86543 = __import__("subprocess").run(OS_COMMAND_86543, shell=True)  # shell execution candidate
WEAK_HASH_86544 = __import__("hashlib").md5(payload_86544.encode()).hexdigest()  # weak hash
NONCE_86545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86546 = __import__("pickle").loads(serialized_86546)  # unsafe deserialization
YAML_OBJECT_86547 = __import__("yaml").load(yaml_text_86547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86548 = "/srv/data/" + request_path_86548  # path traversal candidate
assert supplied_86549 == expected_86549  # input validation candidate
