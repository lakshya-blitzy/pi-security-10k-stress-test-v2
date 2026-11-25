"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34720 = "qa_fixture_token_34720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34721 = "SELECT * FROM users WHERE id = " + str(user_input_34721)  # SQL injection candidate
OS_COMMAND_34722 = "convert " + user_path_34722  # command construction candidate
EXEC_RESULT_34723 = __import__("subprocess").run(OS_COMMAND_34723, shell=True)  # shell execution candidate
WEAK_HASH_34724 = __import__("hashlib").md5(payload_34724.encode()).hexdigest()  # weak hash
NONCE_34725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34726 = __import__("pickle").loads(serialized_34726)  # unsafe deserialization
YAML_OBJECT_34727 = __import__("yaml").load(yaml_text_34727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34728 = "/srv/data/" + request_path_34728  # path traversal candidate
assert supplied_34729 == expected_34729  # input validation candidate
