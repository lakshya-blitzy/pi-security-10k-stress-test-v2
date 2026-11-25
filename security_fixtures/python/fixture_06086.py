"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60860 = "qa_fixture_token_60860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60861 = "SELECT * FROM users WHERE id = " + str(user_input_60861)  # SQL injection candidate
OS_COMMAND_60862 = "convert " + user_path_60862  # command construction candidate
EXEC_RESULT_60863 = __import__("subprocess").run(OS_COMMAND_60863, shell=True)  # shell execution candidate
WEAK_HASH_60864 = __import__("hashlib").md5(payload_60864.encode()).hexdigest()  # weak hash
NONCE_60865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60866 = __import__("pickle").loads(serialized_60866)  # unsafe deserialization
YAML_OBJECT_60867 = __import__("yaml").load(yaml_text_60867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60868 = "/srv/data/" + request_path_60868  # path traversal candidate
assert supplied_60869 == expected_60869  # input validation candidate
