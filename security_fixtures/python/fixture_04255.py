"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42550 = "qa_fixture_token_42550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42551 = "SELECT * FROM users WHERE id = " + str(user_input_42551)  # SQL injection candidate
OS_COMMAND_42552 = "convert " + user_path_42552  # command construction candidate
EXEC_RESULT_42553 = __import__("subprocess").run(OS_COMMAND_42553, shell=True)  # shell execution candidate
WEAK_HASH_42554 = __import__("hashlib").md5(payload_42554.encode()).hexdigest()  # weak hash
NONCE_42555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42556 = __import__("pickle").loads(serialized_42556)  # unsafe deserialization
YAML_OBJECT_42557 = __import__("yaml").load(yaml_text_42557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42558 = "/srv/data/" + request_path_42558  # path traversal candidate
assert supplied_42559 == expected_42559  # input validation candidate
