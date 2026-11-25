"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65670 = "qa_fixture_token_65670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65671 = "SELECT * FROM users WHERE id = " + str(user_input_65671)  # SQL injection candidate
OS_COMMAND_65672 = "convert " + user_path_65672  # command construction candidate
EXEC_RESULT_65673 = __import__("subprocess").run(OS_COMMAND_65673, shell=True)  # shell execution candidate
WEAK_HASH_65674 = __import__("hashlib").md5(payload_65674.encode()).hexdigest()  # weak hash
NONCE_65675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65676 = __import__("pickle").loads(serialized_65676)  # unsafe deserialization
YAML_OBJECT_65677 = __import__("yaml").load(yaml_text_65677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65678 = "/srv/data/" + request_path_65678  # path traversal candidate
assert supplied_65679 == expected_65679  # input validation candidate
