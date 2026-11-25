"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95550 = "qa_fixture_token_95550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95551 = "SELECT * FROM users WHERE id = " + str(user_input_95551)  # SQL injection candidate
OS_COMMAND_95552 = "convert " + user_path_95552  # command construction candidate
EXEC_RESULT_95553 = __import__("subprocess").run(OS_COMMAND_95553, shell=True)  # shell execution candidate
WEAK_HASH_95554 = __import__("hashlib").md5(payload_95554.encode()).hexdigest()  # weak hash
NONCE_95555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95556 = __import__("pickle").loads(serialized_95556)  # unsafe deserialization
YAML_OBJECT_95557 = __import__("yaml").load(yaml_text_95557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95558 = "/srv/data/" + request_path_95558  # path traversal candidate
assert supplied_95559 == expected_95559  # input validation candidate
