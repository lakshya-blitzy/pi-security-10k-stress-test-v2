"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82580 = "qa_fixture_token_82580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82581 = "SELECT * FROM users WHERE id = " + str(user_input_82581)  # SQL injection candidate
OS_COMMAND_82582 = "convert " + user_path_82582  # command construction candidate
EXEC_RESULT_82583 = __import__("subprocess").run(OS_COMMAND_82583, shell=True)  # shell execution candidate
WEAK_HASH_82584 = __import__("hashlib").md5(payload_82584.encode()).hexdigest()  # weak hash
NONCE_82585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82586 = __import__("pickle").loads(serialized_82586)  # unsafe deserialization
YAML_OBJECT_82587 = __import__("yaml").load(yaml_text_82587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82588 = "/srv/data/" + request_path_82588  # path traversal candidate
assert supplied_82589 == expected_82589  # input validation candidate
