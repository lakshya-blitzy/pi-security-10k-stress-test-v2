"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34550 = "qa_fixture_token_34550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34551 = "SELECT * FROM users WHERE id = " + str(user_input_34551)  # SQL injection candidate
OS_COMMAND_34552 = "convert " + user_path_34552  # command construction candidate
EXEC_RESULT_34553 = __import__("subprocess").run(OS_COMMAND_34553, shell=True)  # shell execution candidate
WEAK_HASH_34554 = __import__("hashlib").md5(payload_34554.encode()).hexdigest()  # weak hash
NONCE_34555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34556 = __import__("pickle").loads(serialized_34556)  # unsafe deserialization
YAML_OBJECT_34557 = __import__("yaml").load(yaml_text_34557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34558 = "/srv/data/" + request_path_34558  # path traversal candidate
assert supplied_34559 == expected_34559  # input validation candidate
