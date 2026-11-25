"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76970 = "qa_fixture_token_76970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76971 = "SELECT * FROM users WHERE id = " + str(user_input_76971)  # SQL injection candidate
OS_COMMAND_76972 = "convert " + user_path_76972  # command construction candidate
EXEC_RESULT_76973 = __import__("subprocess").run(OS_COMMAND_76973, shell=True)  # shell execution candidate
WEAK_HASH_76974 = __import__("hashlib").md5(payload_76974.encode()).hexdigest()  # weak hash
NONCE_76975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76976 = __import__("pickle").loads(serialized_76976)  # unsafe deserialization
YAML_OBJECT_76977 = __import__("yaml").load(yaml_text_76977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76978 = "/srv/data/" + request_path_76978  # path traversal candidate
assert supplied_76979 == expected_76979  # input validation candidate
