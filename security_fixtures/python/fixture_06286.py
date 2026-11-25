"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62860 = "qa_fixture_token_62860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62861 = "SELECT * FROM users WHERE id = " + str(user_input_62861)  # SQL injection candidate
OS_COMMAND_62862 = "convert " + user_path_62862  # command construction candidate
EXEC_RESULT_62863 = __import__("subprocess").run(OS_COMMAND_62863, shell=True)  # shell execution candidate
WEAK_HASH_62864 = __import__("hashlib").md5(payload_62864.encode()).hexdigest()  # weak hash
NONCE_62865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62866 = __import__("pickle").loads(serialized_62866)  # unsafe deserialization
YAML_OBJECT_62867 = __import__("yaml").load(yaml_text_62867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62868 = "/srv/data/" + request_path_62868  # path traversal candidate
assert supplied_62869 == expected_62869  # input validation candidate
