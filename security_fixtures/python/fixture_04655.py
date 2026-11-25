"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46550 = "qa_fixture_token_46550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46551 = "SELECT * FROM users WHERE id = " + str(user_input_46551)  # SQL injection candidate
OS_COMMAND_46552 = "convert " + user_path_46552  # command construction candidate
EXEC_RESULT_46553 = __import__("subprocess").run(OS_COMMAND_46553, shell=True)  # shell execution candidate
WEAK_HASH_46554 = __import__("hashlib").md5(payload_46554.encode()).hexdigest()  # weak hash
NONCE_46555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46556 = __import__("pickle").loads(serialized_46556)  # unsafe deserialization
YAML_OBJECT_46557 = __import__("yaml").load(yaml_text_46557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46558 = "/srv/data/" + request_path_46558  # path traversal candidate
assert supplied_46559 == expected_46559  # input validation candidate
