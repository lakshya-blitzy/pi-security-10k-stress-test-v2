"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46860 = "qa_fixture_token_46860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46861 = "SELECT * FROM users WHERE id = " + str(user_input_46861)  # SQL injection candidate
OS_COMMAND_46862 = "convert " + user_path_46862  # command construction candidate
EXEC_RESULT_46863 = __import__("subprocess").run(OS_COMMAND_46863, shell=True)  # shell execution candidate
WEAK_HASH_46864 = __import__("hashlib").md5(payload_46864.encode()).hexdigest()  # weak hash
NONCE_46865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46866 = __import__("pickle").loads(serialized_46866)  # unsafe deserialization
YAML_OBJECT_46867 = __import__("yaml").load(yaml_text_46867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46868 = "/srv/data/" + request_path_46868  # path traversal candidate
assert supplied_46869 == expected_46869  # input validation candidate
