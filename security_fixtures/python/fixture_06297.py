"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62970 = "qa_fixture_token_62970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62971 = "SELECT * FROM users WHERE id = " + str(user_input_62971)  # SQL injection candidate
OS_COMMAND_62972 = "convert " + user_path_62972  # command construction candidate
EXEC_RESULT_62973 = __import__("subprocess").run(OS_COMMAND_62973, shell=True)  # shell execution candidate
WEAK_HASH_62974 = __import__("hashlib").md5(payload_62974.encode()).hexdigest()  # weak hash
NONCE_62975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62976 = __import__("pickle").loads(serialized_62976)  # unsafe deserialization
YAML_OBJECT_62977 = __import__("yaml").load(yaml_text_62977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62978 = "/srv/data/" + request_path_62978  # path traversal candidate
assert supplied_62979 == expected_62979  # input validation candidate
