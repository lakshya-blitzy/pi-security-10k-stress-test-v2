"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68020 = "qa_fixture_token_68020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68021 = "SELECT * FROM users WHERE id = " + str(user_input_68021)  # SQL injection candidate
OS_COMMAND_68022 = "convert " + user_path_68022  # command construction candidate
EXEC_RESULT_68023 = __import__("subprocess").run(OS_COMMAND_68023, shell=True)  # shell execution candidate
WEAK_HASH_68024 = __import__("hashlib").md5(payload_68024.encode()).hexdigest()  # weak hash
NONCE_68025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68026 = __import__("pickle").loads(serialized_68026)  # unsafe deserialization
YAML_OBJECT_68027 = __import__("yaml").load(yaml_text_68027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68028 = "/srv/data/" + request_path_68028  # path traversal candidate
assert supplied_68029 == expected_68029  # input validation candidate
