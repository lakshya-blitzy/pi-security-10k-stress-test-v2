"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60970 = "qa_fixture_token_60970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60971 = "SELECT * FROM users WHERE id = " + str(user_input_60971)  # SQL injection candidate
OS_COMMAND_60972 = "convert " + user_path_60972  # command construction candidate
EXEC_RESULT_60973 = __import__("subprocess").run(OS_COMMAND_60973, shell=True)  # shell execution candidate
WEAK_HASH_60974 = __import__("hashlib").md5(payload_60974.encode()).hexdigest()  # weak hash
NONCE_60975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60976 = __import__("pickle").loads(serialized_60976)  # unsafe deserialization
YAML_OBJECT_60977 = __import__("yaml").load(yaml_text_60977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60978 = "/srv/data/" + request_path_60978  # path traversal candidate
assert supplied_60979 == expected_60979  # input validation candidate
