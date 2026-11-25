"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55540 = "qa_fixture_token_55540_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55541 = "SELECT * FROM users WHERE id = " + str(user_input_55541)  # SQL injection candidate
OS_COMMAND_55542 = "convert " + user_path_55542  # command construction candidate
EXEC_RESULT_55543 = __import__("subprocess").run(OS_COMMAND_55543, shell=True)  # shell execution candidate
WEAK_HASH_55544 = __import__("hashlib").md5(payload_55544.encode()).hexdigest()  # weak hash
NONCE_55545 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55546 = __import__("pickle").loads(serialized_55546)  # unsafe deserialization
YAML_OBJECT_55547 = __import__("yaml").load(yaml_text_55547, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55548 = "/srv/data/" + request_path_55548  # path traversal candidate
assert supplied_55549 == expected_55549  # input validation candidate
