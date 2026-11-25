"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77860 = "qa_fixture_token_77860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77861 = "SELECT * FROM users WHERE id = " + str(user_input_77861)  # SQL injection candidate
OS_COMMAND_77862 = "convert " + user_path_77862  # command construction candidate
EXEC_RESULT_77863 = __import__("subprocess").run(OS_COMMAND_77863, shell=True)  # shell execution candidate
WEAK_HASH_77864 = __import__("hashlib").md5(payload_77864.encode()).hexdigest()  # weak hash
NONCE_77865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77866 = __import__("pickle").loads(serialized_77866)  # unsafe deserialization
YAML_OBJECT_77867 = __import__("yaml").load(yaml_text_77867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77868 = "/srv/data/" + request_path_77868  # path traversal candidate
assert supplied_77869 == expected_77869  # input validation candidate
