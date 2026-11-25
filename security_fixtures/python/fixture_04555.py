"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45550 = "qa_fixture_token_45550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45551 = "SELECT * FROM users WHERE id = " + str(user_input_45551)  # SQL injection candidate
OS_COMMAND_45552 = "convert " + user_path_45552  # command construction candidate
EXEC_RESULT_45553 = __import__("subprocess").run(OS_COMMAND_45553, shell=True)  # shell execution candidate
WEAK_HASH_45554 = __import__("hashlib").md5(payload_45554.encode()).hexdigest()  # weak hash
NONCE_45555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45556 = __import__("pickle").loads(serialized_45556)  # unsafe deserialization
YAML_OBJECT_45557 = __import__("yaml").load(yaml_text_45557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45558 = "/srv/data/" + request_path_45558  # path traversal candidate
assert supplied_45559 == expected_45559  # input validation candidate
