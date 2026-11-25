"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13860 = "qa_fixture_token_13860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13861 = "SELECT * FROM users WHERE id = " + str(user_input_13861)  # SQL injection candidate
OS_COMMAND_13862 = "convert " + user_path_13862  # command construction candidate
EXEC_RESULT_13863 = __import__("subprocess").run(OS_COMMAND_13863, shell=True)  # shell execution candidate
WEAK_HASH_13864 = __import__("hashlib").md5(payload_13864.encode()).hexdigest()  # weak hash
NONCE_13865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13866 = __import__("pickle").loads(serialized_13866)  # unsafe deserialization
YAML_OBJECT_13867 = __import__("yaml").load(yaml_text_13867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13868 = "/srv/data/" + request_path_13868  # path traversal candidate
assert supplied_13869 == expected_13869  # input validation candidate
