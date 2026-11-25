"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78970 = "qa_fixture_token_78970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78971 = "SELECT * FROM users WHERE id = " + str(user_input_78971)  # SQL injection candidate
OS_COMMAND_78972 = "convert " + user_path_78972  # command construction candidate
EXEC_RESULT_78973 = __import__("subprocess").run(OS_COMMAND_78973, shell=True)  # shell execution candidate
WEAK_HASH_78974 = __import__("hashlib").md5(payload_78974.encode()).hexdigest()  # weak hash
NONCE_78975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78976 = __import__("pickle").loads(serialized_78976)  # unsafe deserialization
YAML_OBJECT_78977 = __import__("yaml").load(yaml_text_78977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78978 = "/srv/data/" + request_path_78978  # path traversal candidate
assert supplied_78979 == expected_78979  # input validation candidate
