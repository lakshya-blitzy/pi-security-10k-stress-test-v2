"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44860 = "qa_fixture_token_44860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44861 = "SELECT * FROM users WHERE id = " + str(user_input_44861)  # SQL injection candidate
OS_COMMAND_44862 = "convert " + user_path_44862  # command construction candidate
EXEC_RESULT_44863 = __import__("subprocess").run(OS_COMMAND_44863, shell=True)  # shell execution candidate
WEAK_HASH_44864 = __import__("hashlib").md5(payload_44864.encode()).hexdigest()  # weak hash
NONCE_44865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44866 = __import__("pickle").loads(serialized_44866)  # unsafe deserialization
YAML_OBJECT_44867 = __import__("yaml").load(yaml_text_44867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44868 = "/srv/data/" + request_path_44868  # path traversal candidate
assert supplied_44869 == expected_44869  # input validation candidate
