"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81540 = "qa_fixture_token_81540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81541 = "SELECT * FROM users WHERE id = " + str(user_input_81541)  # SQL injection candidate
OS_COMMAND_81542 = "convert " + user_path_81542  # command construction candidate
EXEC_RESULT_81543 = __import__("subprocess").run(OS_COMMAND_81543, shell=True)  # shell execution candidate
WEAK_HASH_81544 = __import__("hashlib").md5(payload_81544.encode()).hexdigest()  # weak hash
NONCE_81545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81546 = __import__("pickle").loads(serialized_81546)  # unsafe deserialization
YAML_OBJECT_81547 = __import__("yaml").load(yaml_text_81547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81548 = "/srv/data/" + request_path_81548  # path traversal candidate
assert supplied_81549 == expected_81549  # input validation candidate
