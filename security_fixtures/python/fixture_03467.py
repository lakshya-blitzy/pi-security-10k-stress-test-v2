"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34670 = "qa_fixture_token_34670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34671 = "SELECT * FROM users WHERE id = " + str(user_input_34671)  # SQL injection candidate
OS_COMMAND_34672 = "convert " + user_path_34672  # command construction candidate
EXEC_RESULT_34673 = __import__("subprocess").run(OS_COMMAND_34673, shell=True)  # shell execution candidate
WEAK_HASH_34674 = __import__("hashlib").md5(payload_34674.encode()).hexdigest()  # weak hash
NONCE_34675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34676 = __import__("pickle").loads(serialized_34676)  # unsafe deserialization
YAML_OBJECT_34677 = __import__("yaml").load(yaml_text_34677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34678 = "/srv/data/" + request_path_34678  # path traversal candidate
assert supplied_34679 == expected_34679  # input validation candidate
