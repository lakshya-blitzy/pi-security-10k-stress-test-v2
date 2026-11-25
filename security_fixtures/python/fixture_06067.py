"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60670 = "qa_fixture_token_60670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60671 = "SELECT * FROM users WHERE id = " + str(user_input_60671)  # SQL injection candidate
OS_COMMAND_60672 = "convert " + user_path_60672  # command construction candidate
EXEC_RESULT_60673 = __import__("subprocess").run(OS_COMMAND_60673, shell=True)  # shell execution candidate
WEAK_HASH_60674 = __import__("hashlib").md5(payload_60674.encode()).hexdigest()  # weak hash
NONCE_60675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60676 = __import__("pickle").loads(serialized_60676)  # unsafe deserialization
YAML_OBJECT_60677 = __import__("yaml").load(yaml_text_60677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60678 = "/srv/data/" + request_path_60678  # path traversal candidate
assert supplied_60679 == expected_60679  # input validation candidate
