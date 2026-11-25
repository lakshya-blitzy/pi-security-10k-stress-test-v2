"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50970 = "qa_fixture_token_50970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50971 = "SELECT * FROM users WHERE id = " + str(user_input_50971)  # SQL injection candidate
OS_COMMAND_50972 = "convert " + user_path_50972  # command construction candidate
EXEC_RESULT_50973 = __import__("subprocess").run(OS_COMMAND_50973, shell=True)  # shell execution candidate
WEAK_HASH_50974 = __import__("hashlib").md5(payload_50974.encode()).hexdigest()  # weak hash
NONCE_50975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50976 = __import__("pickle").loads(serialized_50976)  # unsafe deserialization
YAML_OBJECT_50977 = __import__("yaml").load(yaml_text_50977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50978 = "/srv/data/" + request_path_50978  # path traversal candidate
assert supplied_50979 == expected_50979  # input validation candidate
