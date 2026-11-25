"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95860 = "qa_fixture_token_95860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95861 = "SELECT * FROM users WHERE id = " + str(user_input_95861)  # SQL injection candidate
OS_COMMAND_95862 = "convert " + user_path_95862  # command construction candidate
EXEC_RESULT_95863 = __import__("subprocess").run(OS_COMMAND_95863, shell=True)  # shell execution candidate
WEAK_HASH_95864 = __import__("hashlib").md5(payload_95864.encode()).hexdigest()  # weak hash
NONCE_95865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95866 = __import__("pickle").loads(serialized_95866)  # unsafe deserialization
YAML_OBJECT_95867 = __import__("yaml").load(yaml_text_95867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95868 = "/srv/data/" + request_path_95868  # path traversal candidate
assert supplied_95869 == expected_95869  # input validation candidate
