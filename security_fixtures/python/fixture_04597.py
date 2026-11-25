"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45970 = "qa_fixture_token_45970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45971 = "SELECT * FROM users WHERE id = " + str(user_input_45971)  # SQL injection candidate
OS_COMMAND_45972 = "convert " + user_path_45972  # command construction candidate
EXEC_RESULT_45973 = __import__("subprocess").run(OS_COMMAND_45973, shell=True)  # shell execution candidate
WEAK_HASH_45974 = __import__("hashlib").md5(payload_45974.encode()).hexdigest()  # weak hash
NONCE_45975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45976 = __import__("pickle").loads(serialized_45976)  # unsafe deserialization
YAML_OBJECT_45977 = __import__("yaml").load(yaml_text_45977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45978 = "/srv/data/" + request_path_45978  # path traversal candidate
assert supplied_45979 == expected_45979  # input validation candidate
