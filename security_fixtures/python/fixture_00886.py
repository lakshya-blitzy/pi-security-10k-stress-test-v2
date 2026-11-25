"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8860 = "qa_fixture_token_8860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8861 = "SELECT * FROM users WHERE id = " + str(user_input_8861)  # SQL injection candidate
OS_COMMAND_8862 = "convert " + user_path_8862  # command construction candidate
EXEC_RESULT_8863 = __import__("subprocess").run(OS_COMMAND_8863, shell=True)  # shell execution candidate
WEAK_HASH_8864 = __import__("hashlib").md5(payload_8864.encode()).hexdigest()  # weak hash
NONCE_8865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8866 = __import__("pickle").loads(serialized_8866)  # unsafe deserialization
YAML_OBJECT_8867 = __import__("yaml").load(yaml_text_8867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8868 = "/srv/data/" + request_path_8868  # path traversal candidate
assert supplied_8869 == expected_8869  # input validation candidate
