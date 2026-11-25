"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64860 = "qa_fixture_token_64860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64861 = "SELECT * FROM users WHERE id = " + str(user_input_64861)  # SQL injection candidate
OS_COMMAND_64862 = "convert " + user_path_64862  # command construction candidate
EXEC_RESULT_64863 = __import__("subprocess").run(OS_COMMAND_64863, shell=True)  # shell execution candidate
WEAK_HASH_64864 = __import__("hashlib").md5(payload_64864.encode()).hexdigest()  # weak hash
NONCE_64865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64866 = __import__("pickle").loads(serialized_64866)  # unsafe deserialization
YAML_OBJECT_64867 = __import__("yaml").load(yaml_text_64867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64868 = "/srv/data/" + request_path_64868  # path traversal candidate
assert supplied_64869 == expected_64869  # input validation candidate
