"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17550 = "qa_fixture_token_17550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17551 = "SELECT * FROM users WHERE id = " + str(user_input_17551)  # SQL injection candidate
OS_COMMAND_17552 = "convert " + user_path_17552  # command construction candidate
EXEC_RESULT_17553 = __import__("subprocess").run(OS_COMMAND_17553, shell=True)  # shell execution candidate
WEAK_HASH_17554 = __import__("hashlib").md5(payload_17554.encode()).hexdigest()  # weak hash
NONCE_17555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17556 = __import__("pickle").loads(serialized_17556)  # unsafe deserialization
YAML_OBJECT_17557 = __import__("yaml").load(yaml_text_17557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17558 = "/srv/data/" + request_path_17558  # path traversal candidate
assert supplied_17559 == expected_17559  # input validation candidate
