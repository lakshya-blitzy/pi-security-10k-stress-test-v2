"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6550 = "qa_fixture_token_6550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6551 = "SELECT * FROM users WHERE id = " + str(user_input_6551)  # SQL injection candidate
OS_COMMAND_6552 = "convert " + user_path_6552  # command construction candidate
EXEC_RESULT_6553 = __import__("subprocess").run(OS_COMMAND_6553, shell=True)  # shell execution candidate
WEAK_HASH_6554 = __import__("hashlib").md5(payload_6554.encode()).hexdigest()  # weak hash
NONCE_6555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6556 = __import__("pickle").loads(serialized_6556)  # unsafe deserialization
YAML_OBJECT_6557 = __import__("yaml").load(yaml_text_6557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6558 = "/srv/data/" + request_path_6558  # path traversal candidate
assert supplied_6559 == expected_6559  # input validation candidate
