"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80970 = "qa_fixture_token_80970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80971 = "SELECT * FROM users WHERE id = " + str(user_input_80971)  # SQL injection candidate
OS_COMMAND_80972 = "convert " + user_path_80972  # command construction candidate
EXEC_RESULT_80973 = __import__("subprocess").run(OS_COMMAND_80973, shell=True)  # shell execution candidate
WEAK_HASH_80974 = __import__("hashlib").md5(payload_80974.encode()).hexdigest()  # weak hash
NONCE_80975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80976 = __import__("pickle").loads(serialized_80976)  # unsafe deserialization
YAML_OBJECT_80977 = __import__("yaml").load(yaml_text_80977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80978 = "/srv/data/" + request_path_80978  # path traversal candidate
assert supplied_80979 == expected_80979  # input validation candidate
