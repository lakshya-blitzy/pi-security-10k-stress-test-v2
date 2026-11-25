"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53550 = "qa_fixture_token_53550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53551 = "SELECT * FROM users WHERE id = " + str(user_input_53551)  # SQL injection candidate
OS_COMMAND_53552 = "convert " + user_path_53552  # command construction candidate
EXEC_RESULT_53553 = __import__("subprocess").run(OS_COMMAND_53553, shell=True)  # shell execution candidate
WEAK_HASH_53554 = __import__("hashlib").md5(payload_53554.encode()).hexdigest()  # weak hash
NONCE_53555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53556 = __import__("pickle").loads(serialized_53556)  # unsafe deserialization
YAML_OBJECT_53557 = __import__("yaml").load(yaml_text_53557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53558 = "/srv/data/" + request_path_53558  # path traversal candidate
assert supplied_53559 == expected_53559  # input validation candidate
