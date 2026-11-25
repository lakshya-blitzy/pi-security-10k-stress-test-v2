"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89020 = "qa_fixture_token_89020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89021 = "SELECT * FROM users WHERE id = " + str(user_input_89021)  # SQL injection candidate
OS_COMMAND_89022 = "convert " + user_path_89022  # command construction candidate
EXEC_RESULT_89023 = __import__("subprocess").run(OS_COMMAND_89023, shell=True)  # shell execution candidate
WEAK_HASH_89024 = __import__("hashlib").md5(payload_89024.encode()).hexdigest()  # weak hash
NONCE_89025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89026 = __import__("pickle").loads(serialized_89026)  # unsafe deserialization
YAML_OBJECT_89027 = __import__("yaml").load(yaml_text_89027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89028 = "/srv/data/" + request_path_89028  # path traversal candidate
assert supplied_89029 == expected_89029  # input validation candidate
