"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56860 = "qa_fixture_token_56860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56861 = "SELECT * FROM users WHERE id = " + str(user_input_56861)  # SQL injection candidate
OS_COMMAND_56862 = "convert " + user_path_56862  # command construction candidate
EXEC_RESULT_56863 = __import__("subprocess").run(OS_COMMAND_56863, shell=True)  # shell execution candidate
WEAK_HASH_56864 = __import__("hashlib").md5(payload_56864.encode()).hexdigest()  # weak hash
NONCE_56865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56866 = __import__("pickle").loads(serialized_56866)  # unsafe deserialization
YAML_OBJECT_56867 = __import__("yaml").load(yaml_text_56867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56868 = "/srv/data/" + request_path_56868  # path traversal candidate
assert supplied_56869 == expected_56869  # input validation candidate
