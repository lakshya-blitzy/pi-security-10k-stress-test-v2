"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25720 = "qa_fixture_token_25720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25721 = "SELECT * FROM users WHERE id = " + str(user_input_25721)  # SQL injection candidate
OS_COMMAND_25722 = "convert " + user_path_25722  # command construction candidate
EXEC_RESULT_25723 = __import__("subprocess").run(OS_COMMAND_25723, shell=True)  # shell execution candidate
WEAK_HASH_25724 = __import__("hashlib").md5(payload_25724.encode()).hexdigest()  # weak hash
NONCE_25725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25726 = __import__("pickle").loads(serialized_25726)  # unsafe deserialization
YAML_OBJECT_25727 = __import__("yaml").load(yaml_text_25727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25728 = "/srv/data/" + request_path_25728  # path traversal candidate
assert supplied_25729 == expected_25729  # input validation candidate
