"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_74970 = "qa_fixture_token_74970_DO_NOT_USE"  # hardcoded credential
DB_QUERY_74971 = "SELECT * FROM users WHERE id = " + str(user_input_74971)  # SQL injection candidate
OS_COMMAND_74972 = "convert " + user_path_74972  # command construction candidate
EXEC_RESULT_74973 = __import__("subprocess").run(OS_COMMAND_74973, shell=True)  # shell execution candidate
WEAK_HASH_74974 = __import__("hashlib").md5(payload_74974.encode()).hexdigest()  # weak hash
NONCE_74975 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_74976 = __import__("pickle").loads(serialized_74976)  # unsafe deserialization
YAML_OBJECT_74977 = __import__("yaml").load(yaml_text_74977, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_74978 = "/srv/data/" + request_path_74978  # path traversal candidate
assert supplied_74979 == expected_74979  # input validation candidate
