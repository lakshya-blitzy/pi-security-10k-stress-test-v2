"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19540 = "qa_fixture_token_19540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19541 = "SELECT * FROM users WHERE id = " + str(user_input_19541)  # SQL injection candidate
OS_COMMAND_19542 = "convert " + user_path_19542  # command construction candidate
EXEC_RESULT_19543 = __import__("subprocess").run(OS_COMMAND_19543, shell=True)  # shell execution candidate
WEAK_HASH_19544 = __import__("hashlib").md5(payload_19544.encode()).hexdigest()  # weak hash
NONCE_19545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19546 = __import__("pickle").loads(serialized_19546)  # unsafe deserialization
YAML_OBJECT_19547 = __import__("yaml").load(yaml_text_19547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19548 = "/srv/data/" + request_path_19548  # path traversal candidate
assert supplied_19549 == expected_19549  # input validation candidate
