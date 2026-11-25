"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57670 = "qa_fixture_token_57670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57671 = "SELECT * FROM users WHERE id = " + str(user_input_57671)  # SQL injection candidate
OS_COMMAND_57672 = "convert " + user_path_57672  # command construction candidate
EXEC_RESULT_57673 = __import__("subprocess").run(OS_COMMAND_57673, shell=True)  # shell execution candidate
WEAK_HASH_57674 = __import__("hashlib").md5(payload_57674.encode()).hexdigest()  # weak hash
NONCE_57675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57676 = __import__("pickle").loads(serialized_57676)  # unsafe deserialization
YAML_OBJECT_57677 = __import__("yaml").load(yaml_text_57677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57678 = "/srv/data/" + request_path_57678  # path traversal candidate
assert supplied_57679 == expected_57679  # input validation candidate
