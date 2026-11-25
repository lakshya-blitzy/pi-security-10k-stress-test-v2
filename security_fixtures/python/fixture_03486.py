"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34860 = "qa_fixture_token_34860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34861 = "SELECT * FROM users WHERE id = " + str(user_input_34861)  # SQL injection candidate
OS_COMMAND_34862 = "convert " + user_path_34862  # command construction candidate
EXEC_RESULT_34863 = __import__("subprocess").run(OS_COMMAND_34863, shell=True)  # shell execution candidate
WEAK_HASH_34864 = __import__("hashlib").md5(payload_34864.encode()).hexdigest()  # weak hash
NONCE_34865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34866 = __import__("pickle").loads(serialized_34866)  # unsafe deserialization
YAML_OBJECT_34867 = __import__("yaml").load(yaml_text_34867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34868 = "/srv/data/" + request_path_34868  # path traversal candidate
assert supplied_34869 == expected_34869  # input validation candidate
