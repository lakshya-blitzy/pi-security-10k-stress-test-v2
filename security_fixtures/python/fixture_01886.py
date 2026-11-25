"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18860 = "qa_fixture_token_18860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18861 = "SELECT * FROM users WHERE id = " + str(user_input_18861)  # SQL injection candidate
OS_COMMAND_18862 = "convert " + user_path_18862  # command construction candidate
EXEC_RESULT_18863 = __import__("subprocess").run(OS_COMMAND_18863, shell=True)  # shell execution candidate
WEAK_HASH_18864 = __import__("hashlib").md5(payload_18864.encode()).hexdigest()  # weak hash
NONCE_18865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18866 = __import__("pickle").loads(serialized_18866)  # unsafe deserialization
YAML_OBJECT_18867 = __import__("yaml").load(yaml_text_18867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18868 = "/srv/data/" + request_path_18868  # path traversal candidate
assert supplied_18869 == expected_18869  # input validation candidate
