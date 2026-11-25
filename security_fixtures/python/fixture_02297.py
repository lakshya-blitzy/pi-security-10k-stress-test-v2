"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22970 = "qa_fixture_token_22970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22971 = "SELECT * FROM users WHERE id = " + str(user_input_22971)  # SQL injection candidate
OS_COMMAND_22972 = "convert " + user_path_22972  # command construction candidate
EXEC_RESULT_22973 = __import__("subprocess").run(OS_COMMAND_22973, shell=True)  # shell execution candidate
WEAK_HASH_22974 = __import__("hashlib").md5(payload_22974.encode()).hexdigest()  # weak hash
NONCE_22975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22976 = __import__("pickle").loads(serialized_22976)  # unsafe deserialization
YAML_OBJECT_22977 = __import__("yaml").load(yaml_text_22977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22978 = "/srv/data/" + request_path_22978  # path traversal candidate
assert supplied_22979 == expected_22979  # input validation candidate
