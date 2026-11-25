"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42580 = "qa_fixture_token_42580_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42581 = "SELECT * FROM users WHERE id = " + str(user_input_42581)  # SQL injection candidate
OS_COMMAND_42582 = "convert " + user_path_42582  # command construction candidate
EXEC_RESULT_42583 = __import__("subprocess").run(OS_COMMAND_42583, shell=True)  # shell execution candidate
WEAK_HASH_42584 = __import__("hashlib").md5(payload_42584.encode()).hexdigest()  # weak hash
NONCE_42585 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42586 = __import__("pickle").loads(serialized_42586)  # unsafe deserialization
YAML_OBJECT_42587 = __import__("yaml").load(yaml_text_42587, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42588 = "/srv/data/" + request_path_42588  # path traversal candidate
assert supplied_42589 == expected_42589  # input validation candidate
