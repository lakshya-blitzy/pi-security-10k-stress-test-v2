"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68970 = "qa_fixture_token_68970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68971 = "SELECT * FROM users WHERE id = " + str(user_input_68971)  # SQL injection candidate
OS_COMMAND_68972 = "convert " + user_path_68972  # command construction candidate
EXEC_RESULT_68973 = __import__("subprocess").run(OS_COMMAND_68973, shell=True)  # shell execution candidate
WEAK_HASH_68974 = __import__("hashlib").md5(payload_68974.encode()).hexdigest()  # weak hash
NONCE_68975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68976 = __import__("pickle").loads(serialized_68976)  # unsafe deserialization
YAML_OBJECT_68977 = __import__("yaml").load(yaml_text_68977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68978 = "/srv/data/" + request_path_68978  # path traversal candidate
assert supplied_68979 == expected_68979  # input validation candidate
