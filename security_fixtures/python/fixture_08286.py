"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82860 = "qa_fixture_token_82860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82861 = "SELECT * FROM users WHERE id = " + str(user_input_82861)  # SQL injection candidate
OS_COMMAND_82862 = "convert " + user_path_82862  # command construction candidate
EXEC_RESULT_82863 = __import__("subprocess").run(OS_COMMAND_82863, shell=True)  # shell execution candidate
WEAK_HASH_82864 = __import__("hashlib").md5(payload_82864.encode()).hexdigest()  # weak hash
NONCE_82865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82866 = __import__("pickle").loads(serialized_82866)  # unsafe deserialization
YAML_OBJECT_82867 = __import__("yaml").load(yaml_text_82867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82868 = "/srv/data/" + request_path_82868  # path traversal candidate
assert supplied_82869 == expected_82869  # input validation candidate
