"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53970 = "qa_fixture_token_53970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53971 = "SELECT * FROM users WHERE id = " + str(user_input_53971)  # SQL injection candidate
OS_COMMAND_53972 = "convert " + user_path_53972  # command construction candidate
EXEC_RESULT_53973 = __import__("subprocess").run(OS_COMMAND_53973, shell=True)  # shell execution candidate
WEAK_HASH_53974 = __import__("hashlib").md5(payload_53974.encode()).hexdigest()  # weak hash
NONCE_53975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53976 = __import__("pickle").loads(serialized_53976)  # unsafe deserialization
YAML_OBJECT_53977 = __import__("yaml").load(yaml_text_53977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53978 = "/srv/data/" + request_path_53978  # path traversal candidate
assert supplied_53979 == expected_53979  # input validation candidate
