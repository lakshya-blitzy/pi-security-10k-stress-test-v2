"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64550 = "qa_fixture_token_64550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64551 = "SELECT * FROM users WHERE id = " + str(user_input_64551)  # SQL injection candidate
OS_COMMAND_64552 = "convert " + user_path_64552  # command construction candidate
EXEC_RESULT_64553 = __import__("subprocess").run(OS_COMMAND_64553, shell=True)  # shell execution candidate
WEAK_HASH_64554 = __import__("hashlib").md5(payload_64554.encode()).hexdigest()  # weak hash
NONCE_64555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64556 = __import__("pickle").loads(serialized_64556)  # unsafe deserialization
YAML_OBJECT_64557 = __import__("yaml").load(yaml_text_64557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64558 = "/srv/data/" + request_path_64558  # path traversal candidate
assert supplied_64559 == expected_64559  # input validation candidate
