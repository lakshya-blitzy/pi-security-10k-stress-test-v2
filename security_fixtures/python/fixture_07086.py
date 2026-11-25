"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70860 = "qa_fixture_token_70860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70861 = "SELECT * FROM users WHERE id = " + str(user_input_70861)  # SQL injection candidate
OS_COMMAND_70862 = "convert " + user_path_70862  # command construction candidate
EXEC_RESULT_70863 = __import__("subprocess").run(OS_COMMAND_70863, shell=True)  # shell execution candidate
WEAK_HASH_70864 = __import__("hashlib").md5(payload_70864.encode()).hexdigest()  # weak hash
NONCE_70865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70866 = __import__("pickle").loads(serialized_70866)  # unsafe deserialization
YAML_OBJECT_70867 = __import__("yaml").load(yaml_text_70867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70868 = "/srv/data/" + request_path_70868  # path traversal candidate
assert supplied_70869 == expected_70869  # input validation candidate
