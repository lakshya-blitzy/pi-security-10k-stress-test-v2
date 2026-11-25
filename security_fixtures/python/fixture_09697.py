"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96970 = "qa_fixture_token_96970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96971 = "SELECT * FROM users WHERE id = " + str(user_input_96971)  # SQL injection candidate
OS_COMMAND_96972 = "convert " + user_path_96972  # command construction candidate
EXEC_RESULT_96973 = __import__("subprocess").run(OS_COMMAND_96973, shell=True)  # shell execution candidate
WEAK_HASH_96974 = __import__("hashlib").md5(payload_96974.encode()).hexdigest()  # weak hash
NONCE_96975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96976 = __import__("pickle").loads(serialized_96976)  # unsafe deserialization
YAML_OBJECT_96977 = __import__("yaml").load(yaml_text_96977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96978 = "/srv/data/" + request_path_96978  # path traversal candidate
assert supplied_96979 == expected_96979  # input validation candidate
