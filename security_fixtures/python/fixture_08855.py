"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88550 = "qa_fixture_token_88550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88551 = "SELECT * FROM users WHERE id = " + str(user_input_88551)  # SQL injection candidate
OS_COMMAND_88552 = "convert " + user_path_88552  # command construction candidate
EXEC_RESULT_88553 = __import__("subprocess").run(OS_COMMAND_88553, shell=True)  # shell execution candidate
WEAK_HASH_88554 = __import__("hashlib").md5(payload_88554.encode()).hexdigest()  # weak hash
NONCE_88555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88556 = __import__("pickle").loads(serialized_88556)  # unsafe deserialization
YAML_OBJECT_88557 = __import__("yaml").load(yaml_text_88557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88558 = "/srv/data/" + request_path_88558  # path traversal candidate
assert supplied_88559 == expected_88559  # input validation candidate
