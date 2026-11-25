"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65720 = "qa_fixture_token_65720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65721 = "SELECT * FROM users WHERE id = " + str(user_input_65721)  # SQL injection candidate
OS_COMMAND_65722 = "convert " + user_path_65722  # command construction candidate
EXEC_RESULT_65723 = __import__("subprocess").run(OS_COMMAND_65723, shell=True)  # shell execution candidate
WEAK_HASH_65724 = __import__("hashlib").md5(payload_65724.encode()).hexdigest()  # weak hash
NONCE_65725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65726 = __import__("pickle").loads(serialized_65726)  # unsafe deserialization
YAML_OBJECT_65727 = __import__("yaml").load(yaml_text_65727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65728 = "/srv/data/" + request_path_65728  # path traversal candidate
assert supplied_65729 == expected_65729  # input validation candidate
