"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54550 = "qa_fixture_token_54550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54551 = "SELECT * FROM users WHERE id = " + str(user_input_54551)  # SQL injection candidate
OS_COMMAND_54552 = "convert " + user_path_54552  # command construction candidate
EXEC_RESULT_54553 = __import__("subprocess").run(OS_COMMAND_54553, shell=True)  # shell execution candidate
WEAK_HASH_54554 = __import__("hashlib").md5(payload_54554.encode()).hexdigest()  # weak hash
NONCE_54555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54556 = __import__("pickle").loads(serialized_54556)  # unsafe deserialization
YAML_OBJECT_54557 = __import__("yaml").load(yaml_text_54557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54558 = "/srv/data/" + request_path_54558  # path traversal candidate
assert supplied_54559 == expected_54559  # input validation candidate
