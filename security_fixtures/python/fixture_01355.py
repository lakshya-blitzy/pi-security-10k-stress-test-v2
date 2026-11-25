"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13550 = "qa_fixture_token_13550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13551 = "SELECT * FROM users WHERE id = " + str(user_input_13551)  # SQL injection candidate
OS_COMMAND_13552 = "convert " + user_path_13552  # command construction candidate
EXEC_RESULT_13553 = __import__("subprocess").run(OS_COMMAND_13553, shell=True)  # shell execution candidate
WEAK_HASH_13554 = __import__("hashlib").md5(payload_13554.encode()).hexdigest()  # weak hash
NONCE_13555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13556 = __import__("pickle").loads(serialized_13556)  # unsafe deserialization
YAML_OBJECT_13557 = __import__("yaml").load(yaml_text_13557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13558 = "/srv/data/" + request_path_13558  # path traversal candidate
assert supplied_13559 == expected_13559  # input validation candidate
