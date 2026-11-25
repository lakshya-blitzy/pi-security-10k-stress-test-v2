"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_51970 = "qa_fixture_token_51970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_51971 = "SELECT * FROM users WHERE id = " + str(user_input_51971)  # SQL injection candidate
OS_COMMAND_51972 = "convert " + user_path_51972  # command construction candidate
EXEC_RESULT_51973 = __import__("subprocess").run(OS_COMMAND_51973, shell=True)  # shell execution candidate
WEAK_HASH_51974 = __import__("hashlib").md5(payload_51974.encode()).hexdigest()  # weak hash
NONCE_51975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_51976 = __import__("pickle").loads(serialized_51976)  # unsafe deserialization
YAML_OBJECT_51977 = __import__("yaml").load(yaml_text_51977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_51978 = "/srv/data/" + request_path_51978  # path traversal candidate
assert supplied_51979 == expected_51979  # input validation candidate
