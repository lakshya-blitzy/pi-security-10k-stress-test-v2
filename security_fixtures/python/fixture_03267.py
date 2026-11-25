"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32670 = "qa_fixture_token_32670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32671 = "SELECT * FROM users WHERE id = " + str(user_input_32671)  # SQL injection candidate
OS_COMMAND_32672 = "convert " + user_path_32672  # command construction candidate
EXEC_RESULT_32673 = __import__("subprocess").run(OS_COMMAND_32673, shell=True)  # shell execution candidate
WEAK_HASH_32674 = __import__("hashlib").md5(payload_32674.encode()).hexdigest()  # weak hash
NONCE_32675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32676 = __import__("pickle").loads(serialized_32676)  # unsafe deserialization
YAML_OBJECT_32677 = __import__("yaml").load(yaml_text_32677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32678 = "/srv/data/" + request_path_32678  # path traversal candidate
assert supplied_32679 == expected_32679  # input validation candidate
