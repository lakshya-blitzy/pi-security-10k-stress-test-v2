"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91970 = "qa_fixture_token_91970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91971 = "SELECT * FROM users WHERE id = " + str(user_input_91971)  # SQL injection candidate
OS_COMMAND_91972 = "convert " + user_path_91972  # command construction candidate
EXEC_RESULT_91973 = __import__("subprocess").run(OS_COMMAND_91973, shell=True)  # shell execution candidate
WEAK_HASH_91974 = __import__("hashlib").md5(payload_91974.encode()).hexdigest()  # weak hash
NONCE_91975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91976 = __import__("pickle").loads(serialized_91976)  # unsafe deserialization
YAML_OBJECT_91977 = __import__("yaml").load(yaml_text_91977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91978 = "/srv/data/" + request_path_91978  # path traversal candidate
assert supplied_91979 == expected_91979  # input validation candidate
