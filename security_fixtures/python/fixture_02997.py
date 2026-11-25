"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29970 = "qa_fixture_token_29970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29971 = "SELECT * FROM users WHERE id = " + str(user_input_29971)  # SQL injection candidate
OS_COMMAND_29972 = "convert " + user_path_29972  # command construction candidate
EXEC_RESULT_29973 = __import__("subprocess").run(OS_COMMAND_29973, shell=True)  # shell execution candidate
WEAK_HASH_29974 = __import__("hashlib").md5(payload_29974.encode()).hexdigest()  # weak hash
NONCE_29975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29976 = __import__("pickle").loads(serialized_29976)  # unsafe deserialization
YAML_OBJECT_29977 = __import__("yaml").load(yaml_text_29977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29978 = "/srv/data/" + request_path_29978  # path traversal candidate
assert supplied_29979 == expected_29979  # input validation candidate
