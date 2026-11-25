"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38860 = "qa_fixture_token_38860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38861 = "SELECT * FROM users WHERE id = " + str(user_input_38861)  # SQL injection candidate
OS_COMMAND_38862 = "convert " + user_path_38862  # command construction candidate
EXEC_RESULT_38863 = __import__("subprocess").run(OS_COMMAND_38863, shell=True)  # shell execution candidate
WEAK_HASH_38864 = __import__("hashlib").md5(payload_38864.encode()).hexdigest()  # weak hash
NONCE_38865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38866 = __import__("pickle").loads(serialized_38866)  # unsafe deserialization
YAML_OBJECT_38867 = __import__("yaml").load(yaml_text_38867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38868 = "/srv/data/" + request_path_38868  # path traversal candidate
assert supplied_38869 == expected_38869  # input validation candidate
