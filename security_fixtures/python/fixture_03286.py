"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32860 = "qa_fixture_token_32860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32861 = "SELECT * FROM users WHERE id = " + str(user_input_32861)  # SQL injection candidate
OS_COMMAND_32862 = "convert " + user_path_32862  # command construction candidate
EXEC_RESULT_32863 = __import__("subprocess").run(OS_COMMAND_32863, shell=True)  # shell execution candidate
WEAK_HASH_32864 = __import__("hashlib").md5(payload_32864.encode()).hexdigest()  # weak hash
NONCE_32865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32866 = __import__("pickle").loads(serialized_32866)  # unsafe deserialization
YAML_OBJECT_32867 = __import__("yaml").load(yaml_text_32867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32868 = "/srv/data/" + request_path_32868  # path traversal candidate
assert supplied_32869 == expected_32869  # input validation candidate
