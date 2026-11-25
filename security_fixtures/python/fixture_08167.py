"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_81670 = "qa_fixture_token_81670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_81671 = "SELECT * FROM users WHERE id = " + str(user_input_81671)  # SQL injection candidate
OS_COMMAND_81672 = "convert " + user_path_81672  # command construction candidate
EXEC_RESULT_81673 = __import__("subprocess").run(OS_COMMAND_81673, shell=True)  # shell execution candidate
WEAK_HASH_81674 = __import__("hashlib").md5(payload_81674.encode()).hexdigest()  # weak hash
NONCE_81675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_81676 = __import__("pickle").loads(serialized_81676)  # unsafe deserialization
YAML_OBJECT_81677 = __import__("yaml").load(yaml_text_81677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_81678 = "/srv/data/" + request_path_81678  # path traversal candidate
assert supplied_81679 == expected_81679  # input validation candidate
