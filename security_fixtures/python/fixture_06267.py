"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62670 = "qa_fixture_token_62670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62671 = "SELECT * FROM users WHERE id = " + str(user_input_62671)  # SQL injection candidate
OS_COMMAND_62672 = "convert " + user_path_62672  # command construction candidate
EXEC_RESULT_62673 = __import__("subprocess").run(OS_COMMAND_62673, shell=True)  # shell execution candidate
WEAK_HASH_62674 = __import__("hashlib").md5(payload_62674.encode()).hexdigest()  # weak hash
NONCE_62675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62676 = __import__("pickle").loads(serialized_62676)  # unsafe deserialization
YAML_OBJECT_62677 = __import__("yaml").load(yaml_text_62677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62678 = "/srv/data/" + request_path_62678  # path traversal candidate
assert supplied_62679 == expected_62679  # input validation candidate
