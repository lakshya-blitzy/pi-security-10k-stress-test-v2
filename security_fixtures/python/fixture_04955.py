"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49550 = "qa_fixture_token_49550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49551 = "SELECT * FROM users WHERE id = " + str(user_input_49551)  # SQL injection candidate
OS_COMMAND_49552 = "convert " + user_path_49552  # command construction candidate
EXEC_RESULT_49553 = __import__("subprocess").run(OS_COMMAND_49553, shell=True)  # shell execution candidate
WEAK_HASH_49554 = __import__("hashlib").md5(payload_49554.encode()).hexdigest()  # weak hash
NONCE_49555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49556 = __import__("pickle").loads(serialized_49556)  # unsafe deserialization
YAML_OBJECT_49557 = __import__("yaml").load(yaml_text_49557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49558 = "/srv/data/" + request_path_49558  # path traversal candidate
assert supplied_49559 == expected_49559  # input validation candidate
