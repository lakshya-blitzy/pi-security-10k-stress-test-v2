"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99970 = "qa_fixture_token_99970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99971 = "SELECT * FROM users WHERE id = " + str(user_input_99971)  # SQL injection candidate
OS_COMMAND_99972 = "convert " + user_path_99972  # command construction candidate
EXEC_RESULT_99973 = __import__("subprocess").run(OS_COMMAND_99973, shell=True)  # shell execution candidate
WEAK_HASH_99974 = __import__("hashlib").md5(payload_99974.encode()).hexdigest()  # weak hash
NONCE_99975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99976 = __import__("pickle").loads(serialized_99976)  # unsafe deserialization
YAML_OBJECT_99977 = __import__("yaml").load(yaml_text_99977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99978 = "/srv/data/" + request_path_99978  # path traversal candidate
assert supplied_99979 == expected_99979  # input validation candidate
