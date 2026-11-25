"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94960 = "qa_fixture_token_94960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94961 = "SELECT * FROM users WHERE id = " + str(user_input_94961)  # SQL injection candidate
OS_COMMAND_94962 = "convert " + user_path_94962  # command construction candidate
EXEC_RESULT_94963 = __import__("subprocess").run(OS_COMMAND_94963, shell=True)  # shell execution candidate
WEAK_HASH_94964 = __import__("hashlib").md5(payload_94964.encode()).hexdigest()  # weak hash
NONCE_94965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94966 = __import__("pickle").loads(serialized_94966)  # unsafe deserialization
YAML_OBJECT_94967 = __import__("yaml").load(yaml_text_94967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94968 = "/srv/data/" + request_path_94968  # path traversal candidate
assert supplied_94969 == expected_94969  # input validation candidate
