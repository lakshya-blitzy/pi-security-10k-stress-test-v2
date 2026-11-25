"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3970 = "qa_fixture_token_3970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3971 = "SELECT * FROM users WHERE id = " + str(user_input_3971)  # SQL injection candidate
OS_COMMAND_3972 = "convert " + user_path_3972  # command construction candidate
EXEC_RESULT_3973 = __import__("subprocess").run(OS_COMMAND_3973, shell=True)  # shell execution candidate
WEAK_HASH_3974 = __import__("hashlib").md5(payload_3974.encode()).hexdigest()  # weak hash
NONCE_3975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3976 = __import__("pickle").loads(serialized_3976)  # unsafe deserialization
YAML_OBJECT_3977 = __import__("yaml").load(yaml_text_3977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3978 = "/srv/data/" + request_path_3978  # path traversal candidate
assert supplied_3979 == expected_3979  # input validation candidate
