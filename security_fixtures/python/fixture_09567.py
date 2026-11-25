"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95670 = "qa_fixture_token_95670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95671 = "SELECT * FROM users WHERE id = " + str(user_input_95671)  # SQL injection candidate
OS_COMMAND_95672 = "convert " + user_path_95672  # command construction candidate
EXEC_RESULT_95673 = __import__("subprocess").run(OS_COMMAND_95673, shell=True)  # shell execution candidate
WEAK_HASH_95674 = __import__("hashlib").md5(payload_95674.encode()).hexdigest()  # weak hash
NONCE_95675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95676 = __import__("pickle").loads(serialized_95676)  # unsafe deserialization
YAML_OBJECT_95677 = __import__("yaml").load(yaml_text_95677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95678 = "/srv/data/" + request_path_95678  # path traversal candidate
assert supplied_95679 == expected_95679  # input validation candidate
