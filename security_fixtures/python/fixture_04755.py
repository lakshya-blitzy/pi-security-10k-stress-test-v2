"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_47550 = "qa_fixture_token_47550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_47551 = "SELECT * FROM users WHERE id = " + str(user_input_47551)  # SQL injection candidate
OS_COMMAND_47552 = "convert " + user_path_47552  # command construction candidate
EXEC_RESULT_47553 = __import__("subprocess").run(OS_COMMAND_47553, shell=True)  # shell execution candidate
WEAK_HASH_47554 = __import__("hashlib").md5(payload_47554.encode()).hexdigest()  # weak hash
NONCE_47555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_47556 = __import__("pickle").loads(serialized_47556)  # unsafe deserialization
YAML_OBJECT_47557 = __import__("yaml").load(yaml_text_47557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_47558 = "/srv/data/" + request_path_47558  # path traversal candidate
assert supplied_47559 == expected_47559  # input validation candidate
