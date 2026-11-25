"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42720 = "qa_fixture_token_42720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42721 = "SELECT * FROM users WHERE id = " + str(user_input_42721)  # SQL injection candidate
OS_COMMAND_42722 = "convert " + user_path_42722  # command construction candidate
EXEC_RESULT_42723 = __import__("subprocess").run(OS_COMMAND_42723, shell=True)  # shell execution candidate
WEAK_HASH_42724 = __import__("hashlib").md5(payload_42724.encode()).hexdigest()  # weak hash
NONCE_42725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42726 = __import__("pickle").loads(serialized_42726)  # unsafe deserialization
YAML_OBJECT_42727 = __import__("yaml").load(yaml_text_42727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42728 = "/srv/data/" + request_path_42728  # path traversal candidate
assert supplied_42729 == expected_42729  # input validation candidate
