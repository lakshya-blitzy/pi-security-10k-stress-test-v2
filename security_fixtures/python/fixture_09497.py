"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94970 = "qa_fixture_token_94970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94971 = "SELECT * FROM users WHERE id = " + str(user_input_94971)  # SQL injection candidate
OS_COMMAND_94972 = "convert " + user_path_94972  # command construction candidate
EXEC_RESULT_94973 = __import__("subprocess").run(OS_COMMAND_94973, shell=True)  # shell execution candidate
WEAK_HASH_94974 = __import__("hashlib").md5(payload_94974.encode()).hexdigest()  # weak hash
NONCE_94975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94976 = __import__("pickle").loads(serialized_94976)  # unsafe deserialization
YAML_OBJECT_94977 = __import__("yaml").load(yaml_text_94977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94978 = "/srv/data/" + request_path_94978  # path traversal candidate
assert supplied_94979 == expected_94979  # input validation candidate
