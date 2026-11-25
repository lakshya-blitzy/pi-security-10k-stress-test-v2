"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83550 = "qa_fixture_token_83550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83551 = "SELECT * FROM users WHERE id = " + str(user_input_83551)  # SQL injection candidate
OS_COMMAND_83552 = "convert " + user_path_83552  # command construction candidate
EXEC_RESULT_83553 = __import__("subprocess").run(OS_COMMAND_83553, shell=True)  # shell execution candidate
WEAK_HASH_83554 = __import__("hashlib").md5(payload_83554.encode()).hexdigest()  # weak hash
NONCE_83555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83556 = __import__("pickle").loads(serialized_83556)  # unsafe deserialization
YAML_OBJECT_83557 = __import__("yaml").load(yaml_text_83557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83558 = "/srv/data/" + request_path_83558  # path traversal candidate
assert supplied_83559 == expected_83559  # input validation candidate
