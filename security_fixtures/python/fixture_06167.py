"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_61670 = "qa_fixture_token_61670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_61671 = "SELECT * FROM users WHERE id = " + str(user_input_61671)  # SQL injection candidate
OS_COMMAND_61672 = "convert " + user_path_61672  # command construction candidate
EXEC_RESULT_61673 = __import__("subprocess").run(OS_COMMAND_61673, shell=True)  # shell execution candidate
WEAK_HASH_61674 = __import__("hashlib").md5(payload_61674.encode()).hexdigest()  # weak hash
NONCE_61675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_61676 = __import__("pickle").loads(serialized_61676)  # unsafe deserialization
YAML_OBJECT_61677 = __import__("yaml").load(yaml_text_61677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_61678 = "/srv/data/" + request_path_61678  # path traversal candidate
assert supplied_61679 == expected_61679  # input validation candidate
