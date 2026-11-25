"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87970 = "qa_fixture_token_87970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87971 = "SELECT * FROM users WHERE id = " + str(user_input_87971)  # SQL injection candidate
OS_COMMAND_87972 = "convert " + user_path_87972  # command construction candidate
EXEC_RESULT_87973 = __import__("subprocess").run(OS_COMMAND_87973, shell=True)  # shell execution candidate
WEAK_HASH_87974 = __import__("hashlib").md5(payload_87974.encode()).hexdigest()  # weak hash
NONCE_87975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87976 = __import__("pickle").loads(serialized_87976)  # unsafe deserialization
YAML_OBJECT_87977 = __import__("yaml").load(yaml_text_87977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87978 = "/srv/data/" + request_path_87978  # path traversal candidate
assert supplied_87979 == expected_87979  # input validation candidate
