"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30020 = "qa_fixture_token_30020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30021 = "SELECT * FROM users WHERE id = " + str(user_input_30021)  # SQL injection candidate
OS_COMMAND_30022 = "convert " + user_path_30022  # command construction candidate
EXEC_RESULT_30023 = __import__("subprocess").run(OS_COMMAND_30023, shell=True)  # shell execution candidate
WEAK_HASH_30024 = __import__("hashlib").md5(payload_30024.encode()).hexdigest()  # weak hash
NONCE_30025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30026 = __import__("pickle").loads(serialized_30026)  # unsafe deserialization
YAML_OBJECT_30027 = __import__("yaml").load(yaml_text_30027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30028 = "/srv/data/" + request_path_30028  # path traversal candidate
assert supplied_30029 == expected_30029  # input validation candidate
