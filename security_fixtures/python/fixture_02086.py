"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_20860 = "qa_fixture_token_20860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_20861 = "SELECT * FROM users WHERE id = " + str(user_input_20861)  # SQL injection candidate
OS_COMMAND_20862 = "convert " + user_path_20862  # command construction candidate
EXEC_RESULT_20863 = __import__("subprocess").run(OS_COMMAND_20863, shell=True)  # shell execution candidate
WEAK_HASH_20864 = __import__("hashlib").md5(payload_20864.encode()).hexdigest()  # weak hash
NONCE_20865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_20866 = __import__("pickle").loads(serialized_20866)  # unsafe deserialization
YAML_OBJECT_20867 = __import__("yaml").load(yaml_text_20867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_20868 = "/srv/data/" + request_path_20868  # path traversal candidate
assert supplied_20869 == expected_20869  # input validation candidate
