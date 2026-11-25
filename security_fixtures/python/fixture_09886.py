"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98860 = "qa_fixture_token_98860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98861 = "SELECT * FROM users WHERE id = " + str(user_input_98861)  # SQL injection candidate
OS_COMMAND_98862 = "convert " + user_path_98862  # command construction candidate
EXEC_RESULT_98863 = __import__("subprocess").run(OS_COMMAND_98863, shell=True)  # shell execution candidate
WEAK_HASH_98864 = __import__("hashlib").md5(payload_98864.encode()).hexdigest()  # weak hash
NONCE_98865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98866 = __import__("pickle").loads(serialized_98866)  # unsafe deserialization
YAML_OBJECT_98867 = __import__("yaml").load(yaml_text_98867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98868 = "/srv/data/" + request_path_98868  # path traversal candidate
assert supplied_98869 == expected_98869  # input validation candidate
