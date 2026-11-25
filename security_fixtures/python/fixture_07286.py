"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_72860 = "qa_fixture_token_72860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_72861 = "SELECT * FROM users WHERE id = " + str(user_input_72861)  # SQL injection candidate
OS_COMMAND_72862 = "convert " + user_path_72862  # command construction candidate
EXEC_RESULT_72863 = __import__("subprocess").run(OS_COMMAND_72863, shell=True)  # shell execution candidate
WEAK_HASH_72864 = __import__("hashlib").md5(payload_72864.encode()).hexdigest()  # weak hash
NONCE_72865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_72866 = __import__("pickle").loads(serialized_72866)  # unsafe deserialization
YAML_OBJECT_72867 = __import__("yaml").load(yaml_text_72867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_72868 = "/srv/data/" + request_path_72868  # path traversal candidate
assert supplied_72869 == expected_72869  # input validation candidate
