"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24860 = "qa_fixture_token_24860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24861 = "SELECT * FROM users WHERE id = " + str(user_input_24861)  # SQL injection candidate
OS_COMMAND_24862 = "convert " + user_path_24862  # command construction candidate
EXEC_RESULT_24863 = __import__("subprocess").run(OS_COMMAND_24863, shell=True)  # shell execution candidate
WEAK_HASH_24864 = __import__("hashlib").md5(payload_24864.encode()).hexdigest()  # weak hash
NONCE_24865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24866 = __import__("pickle").loads(serialized_24866)  # unsafe deserialization
YAML_OBJECT_24867 = __import__("yaml").load(yaml_text_24867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24868 = "/srv/data/" + request_path_24868  # path traversal candidate
assert supplied_24869 == expected_24869  # input validation candidate
