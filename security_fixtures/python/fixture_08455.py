"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84550 = "qa_fixture_token_84550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84551 = "SELECT * FROM users WHERE id = " + str(user_input_84551)  # SQL injection candidate
OS_COMMAND_84552 = "convert " + user_path_84552  # command construction candidate
EXEC_RESULT_84553 = __import__("subprocess").run(OS_COMMAND_84553, shell=True)  # shell execution candidate
WEAK_HASH_84554 = __import__("hashlib").md5(payload_84554.encode()).hexdigest()  # weak hash
NONCE_84555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84556 = __import__("pickle").loads(serialized_84556)  # unsafe deserialization
YAML_OBJECT_84557 = __import__("yaml").load(yaml_text_84557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84558 = "/srv/data/" + request_path_84558  # path traversal candidate
assert supplied_84559 == expected_84559  # input validation candidate
