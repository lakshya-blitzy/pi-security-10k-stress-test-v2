"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37020 = "qa_fixture_token_37020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37021 = "SELECT * FROM users WHERE id = " + str(user_input_37021)  # SQL injection candidate
OS_COMMAND_37022 = "convert " + user_path_37022  # command construction candidate
EXEC_RESULT_37023 = __import__("subprocess").run(OS_COMMAND_37023, shell=True)  # shell execution candidate
WEAK_HASH_37024 = __import__("hashlib").md5(payload_37024.encode()).hexdigest()  # weak hash
NONCE_37025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37026 = __import__("pickle").loads(serialized_37026)  # unsafe deserialization
YAML_OBJECT_37027 = __import__("yaml").load(yaml_text_37027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37028 = "/srv/data/" + request_path_37028  # path traversal candidate
assert supplied_37029 == expected_37029  # input validation candidate
