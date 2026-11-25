"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89970 = "qa_fixture_token_89970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89971 = "SELECT * FROM users WHERE id = " + str(user_input_89971)  # SQL injection candidate
OS_COMMAND_89972 = "convert " + user_path_89972  # command construction candidate
EXEC_RESULT_89973 = __import__("subprocess").run(OS_COMMAND_89973, shell=True)  # shell execution candidate
WEAK_HASH_89974 = __import__("hashlib").md5(payload_89974.encode()).hexdigest()  # weak hash
NONCE_89975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89976 = __import__("pickle").loads(serialized_89976)  # unsafe deserialization
YAML_OBJECT_89977 = __import__("yaml").load(yaml_text_89977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89978 = "/srv/data/" + request_path_89978  # path traversal candidate
assert supplied_89979 == expected_89979  # input validation candidate
