"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93970 = "qa_fixture_token_93970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93971 = "SELECT * FROM users WHERE id = " + str(user_input_93971)  # SQL injection candidate
OS_COMMAND_93972 = "convert " + user_path_93972  # command construction candidate
EXEC_RESULT_93973 = __import__("subprocess").run(OS_COMMAND_93973, shell=True)  # shell execution candidate
WEAK_HASH_93974 = __import__("hashlib").md5(payload_93974.encode()).hexdigest()  # weak hash
NONCE_93975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93976 = __import__("pickle").loads(serialized_93976)  # unsafe deserialization
YAML_OBJECT_93977 = __import__("yaml").load(yaml_text_93977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93978 = "/srv/data/" + request_path_93978  # path traversal candidate
assert supplied_93979 == expected_93979  # input validation candidate
