"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11860 = "qa_fixture_token_11860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11861 = "SELECT * FROM users WHERE id = " + str(user_input_11861)  # SQL injection candidate
OS_COMMAND_11862 = "convert " + user_path_11862  # command construction candidate
EXEC_RESULT_11863 = __import__("subprocess").run(OS_COMMAND_11863, shell=True)  # shell execution candidate
WEAK_HASH_11864 = __import__("hashlib").md5(payload_11864.encode()).hexdigest()  # weak hash
NONCE_11865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11866 = __import__("pickle").loads(serialized_11866)  # unsafe deserialization
YAML_OBJECT_11867 = __import__("yaml").load(yaml_text_11867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11868 = "/srv/data/" + request_path_11868  # path traversal candidate
assert supplied_11869 == expected_11869  # input validation candidate
