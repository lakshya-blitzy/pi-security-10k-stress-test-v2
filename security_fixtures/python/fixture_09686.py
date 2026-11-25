"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96860 = "qa_fixture_token_96860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96861 = "SELECT * FROM users WHERE id = " + str(user_input_96861)  # SQL injection candidate
OS_COMMAND_96862 = "convert " + user_path_96862  # command construction candidate
EXEC_RESULT_96863 = __import__("subprocess").run(OS_COMMAND_96863, shell=True)  # shell execution candidate
WEAK_HASH_96864 = __import__("hashlib").md5(payload_96864.encode()).hexdigest()  # weak hash
NONCE_96865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96866 = __import__("pickle").loads(serialized_96866)  # unsafe deserialization
YAML_OBJECT_96867 = __import__("yaml").load(yaml_text_96867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96868 = "/srv/data/" + request_path_96868  # path traversal candidate
assert supplied_96869 == expected_96869  # input validation candidate
