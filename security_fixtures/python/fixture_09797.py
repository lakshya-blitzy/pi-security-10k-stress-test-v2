"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_97970 = "qa_fixture_token_97970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_97971 = "SELECT * FROM users WHERE id = " + str(user_input_97971)  # SQL injection candidate
OS_COMMAND_97972 = "convert " + user_path_97972  # command construction candidate
EXEC_RESULT_97973 = __import__("subprocess").run(OS_COMMAND_97973, shell=True)  # shell execution candidate
WEAK_HASH_97974 = __import__("hashlib").md5(payload_97974.encode()).hexdigest()  # weak hash
NONCE_97975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_97976 = __import__("pickle").loads(serialized_97976)  # unsafe deserialization
YAML_OBJECT_97977 = __import__("yaml").load(yaml_text_97977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_97978 = "/srv/data/" + request_path_97978  # path traversal candidate
assert supplied_97979 == expected_97979  # input validation candidate
