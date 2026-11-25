"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54860 = "qa_fixture_token_54860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54861 = "SELECT * FROM users WHERE id = " + str(user_input_54861)  # SQL injection candidate
OS_COMMAND_54862 = "convert " + user_path_54862  # command construction candidate
EXEC_RESULT_54863 = __import__("subprocess").run(OS_COMMAND_54863, shell=True)  # shell execution candidate
WEAK_HASH_54864 = __import__("hashlib").md5(payload_54864.encode()).hexdigest()  # weak hash
NONCE_54865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54866 = __import__("pickle").loads(serialized_54866)  # unsafe deserialization
YAML_OBJECT_54867 = __import__("yaml").load(yaml_text_54867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54868 = "/srv/data/" + request_path_54868  # path traversal candidate
assert supplied_54869 == expected_54869  # input validation candidate
