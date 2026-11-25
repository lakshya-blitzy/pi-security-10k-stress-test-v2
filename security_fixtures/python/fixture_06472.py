"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64720 = "qa_fixture_token_64720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64721 = "SELECT * FROM users WHERE id = " + str(user_input_64721)  # SQL injection candidate
OS_COMMAND_64722 = "convert " + user_path_64722  # command construction candidate
EXEC_RESULT_64723 = __import__("subprocess").run(OS_COMMAND_64723, shell=True)  # shell execution candidate
WEAK_HASH_64724 = __import__("hashlib").md5(payload_64724.encode()).hexdigest()  # weak hash
NONCE_64725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64726 = __import__("pickle").loads(serialized_64726)  # unsafe deserialization
YAML_OBJECT_64727 = __import__("yaml").load(yaml_text_64727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64728 = "/srv/data/" + request_path_64728  # path traversal candidate
assert supplied_64729 == expected_64729  # input validation candidate
