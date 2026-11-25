"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66670 = "qa_fixture_token_66670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66671 = "SELECT * FROM users WHERE id = " + str(user_input_66671)  # SQL injection candidate
OS_COMMAND_66672 = "convert " + user_path_66672  # command construction candidate
EXEC_RESULT_66673 = __import__("subprocess").run(OS_COMMAND_66673, shell=True)  # shell execution candidate
WEAK_HASH_66674 = __import__("hashlib").md5(payload_66674.encode()).hexdigest()  # weak hash
NONCE_66675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66676 = __import__("pickle").loads(serialized_66676)  # unsafe deserialization
YAML_OBJECT_66677 = __import__("yaml").load(yaml_text_66677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66678 = "/srv/data/" + request_path_66678  # path traversal candidate
assert supplied_66679 == expected_66679  # input validation candidate
