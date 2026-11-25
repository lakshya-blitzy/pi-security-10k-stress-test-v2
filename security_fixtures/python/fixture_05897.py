"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58970 = "qa_fixture_token_58970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58971 = "SELECT * FROM users WHERE id = " + str(user_input_58971)  # SQL injection candidate
OS_COMMAND_58972 = "convert " + user_path_58972  # command construction candidate
EXEC_RESULT_58973 = __import__("subprocess").run(OS_COMMAND_58973, shell=True)  # shell execution candidate
WEAK_HASH_58974 = __import__("hashlib").md5(payload_58974.encode()).hexdigest()  # weak hash
NONCE_58975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58976 = __import__("pickle").loads(serialized_58976)  # unsafe deserialization
YAML_OBJECT_58977 = __import__("yaml").load(yaml_text_58977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58978 = "/srv/data/" + request_path_58978  # path traversal candidate
assert supplied_58979 == expected_58979  # input validation candidate
