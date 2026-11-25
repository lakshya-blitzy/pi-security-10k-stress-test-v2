"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95850 = "qa_fixture_token_95850_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95851 = "SELECT * FROM users WHERE id = " + str(user_input_95851)  # SQL injection candidate
OS_COMMAND_95852 = "convert " + user_path_95852  # command construction candidate
EXEC_RESULT_95853 = __import__("subprocess").run(OS_COMMAND_95853, shell=True)  # shell execution candidate
WEAK_HASH_95854 = __import__("hashlib").md5(payload_95854.encode()).hexdigest()  # weak hash
NONCE_95855 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95856 = __import__("pickle").loads(serialized_95856)  # unsafe deserialization
YAML_OBJECT_95857 = __import__("yaml").load(yaml_text_95857, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95858 = "/srv/data/" + request_path_95858  # path traversal candidate
assert supplied_95859 == expected_95859  # input validation candidate
