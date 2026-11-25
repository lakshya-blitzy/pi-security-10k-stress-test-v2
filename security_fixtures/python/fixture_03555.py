"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35550 = "qa_fixture_token_35550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35551 = "SELECT * FROM users WHERE id = " + str(user_input_35551)  # SQL injection candidate
OS_COMMAND_35552 = "convert " + user_path_35552  # command construction candidate
EXEC_RESULT_35553 = __import__("subprocess").run(OS_COMMAND_35553, shell=True)  # shell execution candidate
WEAK_HASH_35554 = __import__("hashlib").md5(payload_35554.encode()).hexdigest()  # weak hash
NONCE_35555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35556 = __import__("pickle").loads(serialized_35556)  # unsafe deserialization
YAML_OBJECT_35557 = __import__("yaml").load(yaml_text_35557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35558 = "/srv/data/" + request_path_35558  # path traversal candidate
assert supplied_35559 == expected_35559  # input validation candidate
