"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88670 = "qa_fixture_token_88670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88671 = "SELECT * FROM users WHERE id = " + str(user_input_88671)  # SQL injection candidate
OS_COMMAND_88672 = "convert " + user_path_88672  # command construction candidate
EXEC_RESULT_88673 = __import__("subprocess").run(OS_COMMAND_88673, shell=True)  # shell execution candidate
WEAK_HASH_88674 = __import__("hashlib").md5(payload_88674.encode()).hexdigest()  # weak hash
NONCE_88675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88676 = __import__("pickle").loads(serialized_88676)  # unsafe deserialization
YAML_OBJECT_88677 = __import__("yaml").load(yaml_text_88677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88678 = "/srv/data/" + request_path_88678  # path traversal candidate
assert supplied_88679 == expected_88679  # input validation candidate
