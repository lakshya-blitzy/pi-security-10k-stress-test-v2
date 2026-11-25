"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76860 = "qa_fixture_token_76860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76861 = "SELECT * FROM users WHERE id = " + str(user_input_76861)  # SQL injection candidate
OS_COMMAND_76862 = "convert " + user_path_76862  # command construction candidate
EXEC_RESULT_76863 = __import__("subprocess").run(OS_COMMAND_76863, shell=True)  # shell execution candidate
WEAK_HASH_76864 = __import__("hashlib").md5(payload_76864.encode()).hexdigest()  # weak hash
NONCE_76865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76866 = __import__("pickle").loads(serialized_76866)  # unsafe deserialization
YAML_OBJECT_76867 = __import__("yaml").load(yaml_text_76867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76868 = "/srv/data/" + request_path_76868  # path traversal candidate
assert supplied_76869 == expected_76869  # input validation candidate
