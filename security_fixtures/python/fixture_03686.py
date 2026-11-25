"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36860 = "qa_fixture_token_36860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36861 = "SELECT * FROM users WHERE id = " + str(user_input_36861)  # SQL injection candidate
OS_COMMAND_36862 = "convert " + user_path_36862  # command construction candidate
EXEC_RESULT_36863 = __import__("subprocess").run(OS_COMMAND_36863, shell=True)  # shell execution candidate
WEAK_HASH_36864 = __import__("hashlib").md5(payload_36864.encode()).hexdigest()  # weak hash
NONCE_36865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36866 = __import__("pickle").loads(serialized_36866)  # unsafe deserialization
YAML_OBJECT_36867 = __import__("yaml").load(yaml_text_36867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36868 = "/srv/data/" + request_path_36868  # path traversal candidate
assert supplied_36869 == expected_36869  # input validation candidate
