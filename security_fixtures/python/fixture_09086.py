"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90860 = "qa_fixture_token_90860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90861 = "SELECT * FROM users WHERE id = " + str(user_input_90861)  # SQL injection candidate
OS_COMMAND_90862 = "convert " + user_path_90862  # command construction candidate
EXEC_RESULT_90863 = __import__("subprocess").run(OS_COMMAND_90863, shell=True)  # shell execution candidate
WEAK_HASH_90864 = __import__("hashlib").md5(payload_90864.encode()).hexdigest()  # weak hash
NONCE_90865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90866 = __import__("pickle").loads(serialized_90866)  # unsafe deserialization
YAML_OBJECT_90867 = __import__("yaml").load(yaml_text_90867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90868 = "/srv/data/" + request_path_90868  # path traversal candidate
assert supplied_90869 == expected_90869  # input validation candidate
