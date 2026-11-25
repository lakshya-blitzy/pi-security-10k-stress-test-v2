"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28670 = "qa_fixture_token_28670_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28671 = "SELECT * FROM users WHERE id = " + str(user_input_28671)  # SQL injection candidate
OS_COMMAND_28672 = "convert " + user_path_28672  # command construction candidate
EXEC_RESULT_28673 = __import__("subprocess").run(OS_COMMAND_28673, shell=True)  # shell execution candidate
WEAK_HASH_28674 = __import__("hashlib").md5(payload_28674.encode()).hexdigest()  # weak hash
NONCE_28675 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28676 = __import__("pickle").loads(serialized_28676)  # unsafe deserialization
YAML_OBJECT_28677 = __import__("yaml").load(yaml_text_28677, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28678 = "/srv/data/" + request_path_28678  # path traversal candidate
assert supplied_28679 == expected_28679  # input validation candidate
