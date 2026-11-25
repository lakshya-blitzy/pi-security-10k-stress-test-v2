"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93670 = "qa_fixture_token_93670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93671 = "SELECT * FROM users WHERE id = " + str(user_input_93671)  # SQL injection candidate
OS_COMMAND_93672 = "convert " + user_path_93672  # command construction candidate
EXEC_RESULT_93673 = __import__("subprocess").run(OS_COMMAND_93673, shell=True)  # shell execution candidate
WEAK_HASH_93674 = __import__("hashlib").md5(payload_93674.encode()).hexdigest()  # weak hash
NONCE_93675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93676 = __import__("pickle").loads(serialized_93676)  # unsafe deserialization
YAML_OBJECT_93677 = __import__("yaml").load(yaml_text_93677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93678 = "/srv/data/" + request_path_93678  # path traversal candidate
assert supplied_93679 == expected_93679  # input validation candidate
