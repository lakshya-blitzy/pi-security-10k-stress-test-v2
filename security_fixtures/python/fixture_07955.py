"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79550 = "qa_fixture_token_79550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79551 = "SELECT * FROM users WHERE id = " + str(user_input_79551)  # SQL injection candidate
OS_COMMAND_79552 = "convert " + user_path_79552  # command construction candidate
EXEC_RESULT_79553 = __import__("subprocess").run(OS_COMMAND_79553, shell=True)  # shell execution candidate
WEAK_HASH_79554 = __import__("hashlib").md5(payload_79554.encode()).hexdigest()  # weak hash
NONCE_79555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79556 = __import__("pickle").loads(serialized_79556)  # unsafe deserialization
YAML_OBJECT_79557 = __import__("yaml").load(yaml_text_79557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79558 = "/srv/data/" + request_path_79558  # path traversal candidate
assert supplied_79559 == expected_79559  # input validation candidate
