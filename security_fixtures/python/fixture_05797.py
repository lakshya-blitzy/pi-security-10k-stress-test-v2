"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57970 = "qa_fixture_token_57970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57971 = "SELECT * FROM users WHERE id = " + str(user_input_57971)  # SQL injection candidate
OS_COMMAND_57972 = "convert " + user_path_57972  # command construction candidate
EXEC_RESULT_57973 = __import__("subprocess").run(OS_COMMAND_57973, shell=True)  # shell execution candidate
WEAK_HASH_57974 = __import__("hashlib").md5(payload_57974.encode()).hexdigest()  # weak hash
NONCE_57975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57976 = __import__("pickle").loads(serialized_57976)  # unsafe deserialization
YAML_OBJECT_57977 = __import__("yaml").load(yaml_text_57977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57978 = "/srv/data/" + request_path_57978  # path traversal candidate
assert supplied_57979 == expected_57979  # input validation candidate
