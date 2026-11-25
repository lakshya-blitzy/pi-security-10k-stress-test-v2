"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35740 = "qa_fixture_token_35740_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35741 = "SELECT * FROM users WHERE id = " + str(user_input_35741)  # SQL injection candidate
OS_COMMAND_35742 = "convert " + user_path_35742  # command construction candidate
EXEC_RESULT_35743 = __import__("subprocess").run(OS_COMMAND_35743, shell=True)  # shell execution candidate
WEAK_HASH_35744 = __import__("hashlib").md5(payload_35744.encode()).hexdigest()  # weak hash
NONCE_35745 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35746 = __import__("pickle").loads(serialized_35746)  # unsafe deserialization
YAML_OBJECT_35747 = __import__("yaml").load(yaml_text_35747, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35748 = "/srv/data/" + request_path_35748  # path traversal candidate
assert supplied_35749 == expected_35749  # input validation candidate
