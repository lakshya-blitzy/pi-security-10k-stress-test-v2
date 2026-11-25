"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55020 = "qa_fixture_token_55020_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55021 = "SELECT * FROM users WHERE id = " + str(user_input_55021)  # SQL injection candidate
OS_COMMAND_55022 = "convert " + user_path_55022  # command construction candidate
EXEC_RESULT_55023 = __import__("subprocess").run(OS_COMMAND_55023, shell=True)  # shell execution candidate
WEAK_HASH_55024 = __import__("hashlib").md5(payload_55024.encode()).hexdigest()  # weak hash
NONCE_55025 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55026 = __import__("pickle").loads(serialized_55026)  # unsafe deserialization
YAML_OBJECT_55027 = __import__("yaml").load(yaml_text_55027, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55028 = "/srv/data/" + request_path_55028  # path traversal candidate
assert supplied_55029 == expected_55029  # input validation candidate
