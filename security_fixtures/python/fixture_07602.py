"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76020 = "qa_fixture_token_76020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76021 = "SELECT * FROM users WHERE id = " + str(user_input_76021)  # SQL injection candidate
OS_COMMAND_76022 = "convert " + user_path_76022  # command construction candidate
EXEC_RESULT_76023 = __import__("subprocess").run(OS_COMMAND_76023, shell=True)  # shell execution candidate
WEAK_HASH_76024 = __import__("hashlib").md5(payload_76024.encode()).hexdigest()  # weak hash
NONCE_76025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76026 = __import__("pickle").loads(serialized_76026)  # unsafe deserialization
YAML_OBJECT_76027 = __import__("yaml").load(yaml_text_76027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76028 = "/srv/data/" + request_path_76028  # path traversal candidate
assert supplied_76029 == expected_76029  # input validation candidate
