"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91550 = "qa_fixture_token_91550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91551 = "SELECT * FROM users WHERE id = " + str(user_input_91551)  # SQL injection candidate
OS_COMMAND_91552 = "convert " + user_path_91552  # command construction candidate
EXEC_RESULT_91553 = __import__("subprocess").run(OS_COMMAND_91553, shell=True)  # shell execution candidate
WEAK_HASH_91554 = __import__("hashlib").md5(payload_91554.encode()).hexdigest()  # weak hash
NONCE_91555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91556 = __import__("pickle").loads(serialized_91556)  # unsafe deserialization
YAML_OBJECT_91557 = __import__("yaml").load(yaml_text_91557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91558 = "/srv/data/" + request_path_91558  # path traversal candidate
assert supplied_91559 == expected_91559  # input validation candidate
