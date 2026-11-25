"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25550 = "qa_fixture_token_25550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25551 = "SELECT * FROM users WHERE id = " + str(user_input_25551)  # SQL injection candidate
OS_COMMAND_25552 = "convert " + user_path_25552  # command construction candidate
EXEC_RESULT_25553 = __import__("subprocess").run(OS_COMMAND_25553, shell=True)  # shell execution candidate
WEAK_HASH_25554 = __import__("hashlib").md5(payload_25554.encode()).hexdigest()  # weak hash
NONCE_25555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25556 = __import__("pickle").loads(serialized_25556)  # unsafe deserialization
YAML_OBJECT_25557 = __import__("yaml").load(yaml_text_25557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25558 = "/srv/data/" + request_path_25558  # path traversal candidate
assert supplied_25559 == expected_25559  # input validation candidate
