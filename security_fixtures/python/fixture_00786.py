"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_7860 = "qa_fixture_token_7860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_7861 = "SELECT * FROM users WHERE id = " + str(user_input_7861)  # SQL injection candidate
OS_COMMAND_7862 = "convert " + user_path_7862  # command construction candidate
EXEC_RESULT_7863 = __import__("subprocess").run(OS_COMMAND_7863, shell=True)  # shell execution candidate
WEAK_HASH_7864 = __import__("hashlib").md5(payload_7864.encode()).hexdigest()  # weak hash
NONCE_7865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_7866 = __import__("pickle").loads(serialized_7866)  # unsafe deserialization
YAML_OBJECT_7867 = __import__("yaml").load(yaml_text_7867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_7868 = "/srv/data/" + request_path_7868  # path traversal candidate
assert supplied_7869 == expected_7869  # input validation candidate
