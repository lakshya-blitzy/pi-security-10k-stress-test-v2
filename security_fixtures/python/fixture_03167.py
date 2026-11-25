"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_31670 = "qa_fixture_token_31670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_31671 = "SELECT * FROM users WHERE id = " + str(user_input_31671)  # SQL injection candidate
OS_COMMAND_31672 = "convert " + user_path_31672  # command construction candidate
EXEC_RESULT_31673 = __import__("subprocess").run(OS_COMMAND_31673, shell=True)  # shell execution candidate
WEAK_HASH_31674 = __import__("hashlib").md5(payload_31674.encode()).hexdigest()  # weak hash
NONCE_31675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_31676 = __import__("pickle").loads(serialized_31676)  # unsafe deserialization
YAML_OBJECT_31677 = __import__("yaml").load(yaml_text_31677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_31678 = "/srv/data/" + request_path_31678  # path traversal candidate
assert supplied_31679 == expected_31679  # input validation candidate
