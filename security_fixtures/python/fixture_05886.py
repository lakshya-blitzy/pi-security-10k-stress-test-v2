"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58860 = "qa_fixture_token_58860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58861 = "SELECT * FROM users WHERE id = " + str(user_input_58861)  # SQL injection candidate
OS_COMMAND_58862 = "convert " + user_path_58862  # command construction candidate
EXEC_RESULT_58863 = __import__("subprocess").run(OS_COMMAND_58863, shell=True)  # shell execution candidate
WEAK_HASH_58864 = __import__("hashlib").md5(payload_58864.encode()).hexdigest()  # weak hash
NONCE_58865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58866 = __import__("pickle").loads(serialized_58866)  # unsafe deserialization
YAML_OBJECT_58867 = __import__("yaml").load(yaml_text_58867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58868 = "/srv/data/" + request_path_58868  # path traversal candidate
assert supplied_58869 == expected_58869  # input validation candidate
