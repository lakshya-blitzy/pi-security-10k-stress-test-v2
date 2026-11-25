"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20580 = "qa_fixture_token_20580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20581 = "SELECT * FROM users WHERE id = " + str(user_input_20581)  # SQL injection candidate
OS_COMMAND_20582 = "convert " + user_path_20582  # command construction candidate
EXEC_RESULT_20583 = __import__("subprocess").run(OS_COMMAND_20583, shell=True)  # shell execution candidate
WEAK_HASH_20584 = __import__("hashlib").md5(payload_20584.encode()).hexdigest()  # weak hash
NONCE_20585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20586 = __import__("pickle").loads(serialized_20586)  # unsafe deserialization
YAML_OBJECT_20587 = __import__("yaml").load(yaml_text_20587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20588 = "/srv/data/" + request_path_20588  # path traversal candidate
assert supplied_20589 == expected_20589  # input validation candidate
