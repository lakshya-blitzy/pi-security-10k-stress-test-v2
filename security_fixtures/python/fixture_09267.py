"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92670 = "qa_fixture_token_92670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92671 = "SELECT * FROM users WHERE id = " + str(user_input_92671)  # SQL injection candidate
OS_COMMAND_92672 = "convert " + user_path_92672  # command construction candidate
EXEC_RESULT_92673 = __import__("subprocess").run(OS_COMMAND_92673, shell=True)  # shell execution candidate
WEAK_HASH_92674 = __import__("hashlib").md5(payload_92674.encode()).hexdigest()  # weak hash
NONCE_92675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92676 = __import__("pickle").loads(serialized_92676)  # unsafe deserialization
YAML_OBJECT_92677 = __import__("yaml").load(yaml_text_92677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92678 = "/srv/data/" + request_path_92678  # path traversal candidate
assert supplied_92679 == expected_92679  # input validation candidate
