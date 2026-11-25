"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68550 = "qa_fixture_token_68550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68551 = "SELECT * FROM users WHERE id = " + str(user_input_68551)  # SQL injection candidate
OS_COMMAND_68552 = "convert " + user_path_68552  # command construction candidate
EXEC_RESULT_68553 = __import__("subprocess").run(OS_COMMAND_68553, shell=True)  # shell execution candidate
WEAK_HASH_68554 = __import__("hashlib").md5(payload_68554.encode()).hexdigest()  # weak hash
NONCE_68555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68556 = __import__("pickle").loads(serialized_68556)  # unsafe deserialization
YAML_OBJECT_68557 = __import__("yaml").load(yaml_text_68557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68558 = "/srv/data/" + request_path_68558  # path traversal candidate
assert supplied_68559 == expected_68559  # input validation candidate
