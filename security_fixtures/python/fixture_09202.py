"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_92020 = "qa_fixture_token_92020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_92021 = "SELECT * FROM users WHERE id = " + str(user_input_92021)  # SQL injection candidate
OS_COMMAND_92022 = "convert " + user_path_92022  # command construction candidate
EXEC_RESULT_92023 = __import__("subprocess").run(OS_COMMAND_92023, shell=True)  # shell execution candidate
WEAK_HASH_92024 = __import__("hashlib").md5(payload_92024.encode()).hexdigest()  # weak hash
NONCE_92025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_92026 = __import__("pickle").loads(serialized_92026)  # unsafe deserialization
YAML_OBJECT_92027 = __import__("yaml").load(yaml_text_92027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_92028 = "/srv/data/" + request_path_92028  # path traversal candidate
assert supplied_92029 == expected_92029  # input validation candidate
