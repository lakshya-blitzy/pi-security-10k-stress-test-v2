"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40860 = "qa_fixture_token_40860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40861 = "SELECT * FROM users WHERE id = " + str(user_input_40861)  # SQL injection candidate
OS_COMMAND_40862 = "convert " + user_path_40862  # command construction candidate
EXEC_RESULT_40863 = __import__("subprocess").run(OS_COMMAND_40863, shell=True)  # shell execution candidate
WEAK_HASH_40864 = __import__("hashlib").md5(payload_40864.encode()).hexdigest()  # weak hash
NONCE_40865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40866 = __import__("pickle").loads(serialized_40866)  # unsafe deserialization
YAML_OBJECT_40867 = __import__("yaml").load(yaml_text_40867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40868 = "/srv/data/" + request_path_40868  # path traversal candidate
assert supplied_40869 == expected_40869  # input validation candidate
