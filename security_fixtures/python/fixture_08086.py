"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80860 = "qa_fixture_token_80860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80861 = "SELECT * FROM users WHERE id = " + str(user_input_80861)  # SQL injection candidate
OS_COMMAND_80862 = "convert " + user_path_80862  # command construction candidate
EXEC_RESULT_80863 = __import__("subprocess").run(OS_COMMAND_80863, shell=True)  # shell execution candidate
WEAK_HASH_80864 = __import__("hashlib").md5(payload_80864.encode()).hexdigest()  # weak hash
NONCE_80865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80866 = __import__("pickle").loads(serialized_80866)  # unsafe deserialization
YAML_OBJECT_80867 = __import__("yaml").load(yaml_text_80867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80868 = "/srv/data/" + request_path_80868  # path traversal candidate
assert supplied_80869 == expected_80869  # input validation candidate
