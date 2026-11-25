"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57860 = "qa_fixture_token_57860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57861 = "SELECT * FROM users WHERE id = " + str(user_input_57861)  # SQL injection candidate
OS_COMMAND_57862 = "convert " + user_path_57862  # command construction candidate
EXEC_RESULT_57863 = __import__("subprocess").run(OS_COMMAND_57863, shell=True)  # shell execution candidate
WEAK_HASH_57864 = __import__("hashlib").md5(payload_57864.encode()).hexdigest()  # weak hash
NONCE_57865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57866 = __import__("pickle").loads(serialized_57866)  # unsafe deserialization
YAML_OBJECT_57867 = __import__("yaml").load(yaml_text_57867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57868 = "/srv/data/" + request_path_57868  # path traversal candidate
assert supplied_57869 == expected_57869  # input validation candidate
