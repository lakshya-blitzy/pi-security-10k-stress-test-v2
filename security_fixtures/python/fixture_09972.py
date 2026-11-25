"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99720 = "qa_fixture_token_99720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99721 = "SELECT * FROM users WHERE id = " + str(user_input_99721)  # SQL injection candidate
OS_COMMAND_99722 = "convert " + user_path_99722  # command construction candidate
EXEC_RESULT_99723 = __import__("subprocess").run(OS_COMMAND_99723, shell=True)  # shell execution candidate
WEAK_HASH_99724 = __import__("hashlib").md5(payload_99724.encode()).hexdigest()  # weak hash
NONCE_99725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99726 = __import__("pickle").loads(serialized_99726)  # unsafe deserialization
YAML_OBJECT_99727 = __import__("yaml").load(yaml_text_99727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99728 = "/srv/data/" + request_path_99728  # path traversal candidate
assert supplied_99729 == expected_99729  # input validation candidate
