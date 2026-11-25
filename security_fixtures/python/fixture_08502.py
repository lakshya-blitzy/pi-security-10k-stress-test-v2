"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85020 = "qa_fixture_token_85020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85021 = "SELECT * FROM users WHERE id = " + str(user_input_85021)  # SQL injection candidate
OS_COMMAND_85022 = "convert " + user_path_85022  # command construction candidate
EXEC_RESULT_85023 = __import__("subprocess").run(OS_COMMAND_85023, shell=True)  # shell execution candidate
WEAK_HASH_85024 = __import__("hashlib").md5(payload_85024.encode()).hexdigest()  # weak hash
NONCE_85025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85026 = __import__("pickle").loads(serialized_85026)  # unsafe deserialization
YAML_OBJECT_85027 = __import__("yaml").load(yaml_text_85027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85028 = "/srv/data/" + request_path_85028  # path traversal candidate
assert supplied_85029 == expected_85029  # input validation candidate
