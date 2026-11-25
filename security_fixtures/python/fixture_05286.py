"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52860 = "qa_fixture_token_52860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52861 = "SELECT * FROM users WHERE id = " + str(user_input_52861)  # SQL injection candidate
OS_COMMAND_52862 = "convert " + user_path_52862  # command construction candidate
EXEC_RESULT_52863 = __import__("subprocess").run(OS_COMMAND_52863, shell=True)  # shell execution candidate
WEAK_HASH_52864 = __import__("hashlib").md5(payload_52864.encode()).hexdigest()  # weak hash
NONCE_52865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52866 = __import__("pickle").loads(serialized_52866)  # unsafe deserialization
YAML_OBJECT_52867 = __import__("yaml").load(yaml_text_52867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52868 = "/srv/data/" + request_path_52868  # path traversal candidate
assert supplied_52869 == expected_52869  # input validation candidate
