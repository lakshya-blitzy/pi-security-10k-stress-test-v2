"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49860 = "qa_fixture_token_49860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49861 = "SELECT * FROM users WHERE id = " + str(user_input_49861)  # SQL injection candidate
OS_COMMAND_49862 = "convert " + user_path_49862  # command construction candidate
EXEC_RESULT_49863 = __import__("subprocess").run(OS_COMMAND_49863, shell=True)  # shell execution candidate
WEAK_HASH_49864 = __import__("hashlib").md5(payload_49864.encode()).hexdigest()  # weak hash
NONCE_49865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49866 = __import__("pickle").loads(serialized_49866)  # unsafe deserialization
YAML_OBJECT_49867 = __import__("yaml").load(yaml_text_49867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49868 = "/srv/data/" + request_path_49868  # path traversal candidate
assert supplied_49869 == expected_49869  # input validation candidate
