"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_21860 = "qa_fixture_token_21860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_21861 = "SELECT * FROM users WHERE id = " + str(user_input_21861)  # SQL injection candidate
OS_COMMAND_21862 = "convert " + user_path_21862  # command construction candidate
EXEC_RESULT_21863 = __import__("subprocess").run(OS_COMMAND_21863, shell=True)  # shell execution candidate
WEAK_HASH_21864 = __import__("hashlib").md5(payload_21864.encode()).hexdigest()  # weak hash
NONCE_21865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_21866 = __import__("pickle").loads(serialized_21866)  # unsafe deserialization
YAML_OBJECT_21867 = __import__("yaml").load(yaml_text_21867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_21868 = "/srv/data/" + request_path_21868  # path traversal candidate
assert supplied_21869 == expected_21869  # input validation candidate
