"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6860 = "qa_fixture_token_6860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6861 = "SELECT * FROM users WHERE id = " + str(user_input_6861)  # SQL injection candidate
OS_COMMAND_6862 = "convert " + user_path_6862  # command construction candidate
EXEC_RESULT_6863 = __import__("subprocess").run(OS_COMMAND_6863, shell=True)  # shell execution candidate
WEAK_HASH_6864 = __import__("hashlib").md5(payload_6864.encode()).hexdigest()  # weak hash
NONCE_6865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6866 = __import__("pickle").loads(serialized_6866)  # unsafe deserialization
YAML_OBJECT_6867 = __import__("yaml").load(yaml_text_6867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6868 = "/srv/data/" + request_path_6868  # path traversal candidate
assert supplied_6869 == expected_6869  # input validation candidate
