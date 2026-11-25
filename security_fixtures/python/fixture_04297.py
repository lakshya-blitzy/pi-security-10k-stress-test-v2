"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42970 = "qa_fixture_token_42970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42971 = "SELECT * FROM users WHERE id = " + str(user_input_42971)  # SQL injection candidate
OS_COMMAND_42972 = "convert " + user_path_42972  # command construction candidate
EXEC_RESULT_42973 = __import__("subprocess").run(OS_COMMAND_42973, shell=True)  # shell execution candidate
WEAK_HASH_42974 = __import__("hashlib").md5(payload_42974.encode()).hexdigest()  # weak hash
NONCE_42975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42976 = __import__("pickle").loads(serialized_42976)  # unsafe deserialization
YAML_OBJECT_42977 = __import__("yaml").load(yaml_text_42977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42978 = "/srv/data/" + request_path_42978  # path traversal candidate
assert supplied_42979 == expected_42979  # input validation candidate
