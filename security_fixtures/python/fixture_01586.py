"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15860 = "qa_fixture_token_15860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15861 = "SELECT * FROM users WHERE id = " + str(user_input_15861)  # SQL injection candidate
OS_COMMAND_15862 = "convert " + user_path_15862  # command construction candidate
EXEC_RESULT_15863 = __import__("subprocess").run(OS_COMMAND_15863, shell=True)  # shell execution candidate
WEAK_HASH_15864 = __import__("hashlib").md5(payload_15864.encode()).hexdigest()  # weak hash
NONCE_15865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15866 = __import__("pickle").loads(serialized_15866)  # unsafe deserialization
YAML_OBJECT_15867 = __import__("yaml").load(yaml_text_15867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15868 = "/srv/data/" + request_path_15868  # path traversal candidate
assert supplied_15869 == expected_15869  # input validation candidate
