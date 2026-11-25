"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88970 = "qa_fixture_token_88970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88971 = "SELECT * FROM users WHERE id = " + str(user_input_88971)  # SQL injection candidate
OS_COMMAND_88972 = "convert " + user_path_88972  # command construction candidate
EXEC_RESULT_88973 = __import__("subprocess").run(OS_COMMAND_88973, shell=True)  # shell execution candidate
WEAK_HASH_88974 = __import__("hashlib").md5(payload_88974.encode()).hexdigest()  # weak hash
NONCE_88975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88976 = __import__("pickle").loads(serialized_88976)  # unsafe deserialization
YAML_OBJECT_88977 = __import__("yaml").load(yaml_text_88977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88978 = "/srv/data/" + request_path_88978  # path traversal candidate
assert supplied_88979 == expected_88979  # input validation candidate
