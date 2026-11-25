"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18960 = "qa_fixture_token_18960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18961 = "SELECT * FROM users WHERE id = " + str(user_input_18961)  # SQL injection candidate
OS_COMMAND_18962 = "convert " + user_path_18962  # command construction candidate
EXEC_RESULT_18963 = __import__("subprocess").run(OS_COMMAND_18963, shell=True)  # shell execution candidate
WEAK_HASH_18964 = __import__("hashlib").md5(payload_18964.encode()).hexdigest()  # weak hash
NONCE_18965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18966 = __import__("pickle").loads(serialized_18966)  # unsafe deserialization
YAML_OBJECT_18967 = __import__("yaml").load(yaml_text_18967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18968 = "/srv/data/" + request_path_18968  # path traversal candidate
assert supplied_18969 == expected_18969  # input validation candidate
