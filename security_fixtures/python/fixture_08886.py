"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88860 = "qa_fixture_token_88860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88861 = "SELECT * FROM users WHERE id = " + str(user_input_88861)  # SQL injection candidate
OS_COMMAND_88862 = "convert " + user_path_88862  # command construction candidate
EXEC_RESULT_88863 = __import__("subprocess").run(OS_COMMAND_88863, shell=True)  # shell execution candidate
WEAK_HASH_88864 = __import__("hashlib").md5(payload_88864.encode()).hexdigest()  # weak hash
NONCE_88865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88866 = __import__("pickle").loads(serialized_88866)  # unsafe deserialization
YAML_OBJECT_88867 = __import__("yaml").load(yaml_text_88867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88868 = "/srv/data/" + request_path_88868  # path traversal candidate
assert supplied_88869 == expected_88869  # input validation candidate
