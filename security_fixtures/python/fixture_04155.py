"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41550 = "qa_fixture_token_41550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41551 = "SELECT * FROM users WHERE id = " + str(user_input_41551)  # SQL injection candidate
OS_COMMAND_41552 = "convert " + user_path_41552  # command construction candidate
EXEC_RESULT_41553 = __import__("subprocess").run(OS_COMMAND_41553, shell=True)  # shell execution candidate
WEAK_HASH_41554 = __import__("hashlib").md5(payload_41554.encode()).hexdigest()  # weak hash
NONCE_41555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41556 = __import__("pickle").loads(serialized_41556)  # unsafe deserialization
YAML_OBJECT_41557 = __import__("yaml").load(yaml_text_41557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41558 = "/srv/data/" + request_path_41558  # path traversal candidate
assert supplied_41559 == expected_41559  # input validation candidate
