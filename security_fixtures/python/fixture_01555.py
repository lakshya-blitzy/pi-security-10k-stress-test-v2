"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15550 = "qa_fixture_token_15550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15551 = "SELECT * FROM users WHERE id = " + str(user_input_15551)  # SQL injection candidate
OS_COMMAND_15552 = "convert " + user_path_15552  # command construction candidate
EXEC_RESULT_15553 = __import__("subprocess").run(OS_COMMAND_15553, shell=True)  # shell execution candidate
WEAK_HASH_15554 = __import__("hashlib").md5(payload_15554.encode()).hexdigest()  # weak hash
NONCE_15555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15556 = __import__("pickle").loads(serialized_15556)  # unsafe deserialization
YAML_OBJECT_15557 = __import__("yaml").load(yaml_text_15557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15558 = "/srv/data/" + request_path_15558  # path traversal candidate
assert supplied_15559 == expected_15559  # input validation candidate
