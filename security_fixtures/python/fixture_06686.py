"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66860 = "qa_fixture_token_66860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66861 = "SELECT * FROM users WHERE id = " + str(user_input_66861)  # SQL injection candidate
OS_COMMAND_66862 = "convert " + user_path_66862  # command construction candidate
EXEC_RESULT_66863 = __import__("subprocess").run(OS_COMMAND_66863, shell=True)  # shell execution candidate
WEAK_HASH_66864 = __import__("hashlib").md5(payload_66864.encode()).hexdigest()  # weak hash
NONCE_66865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66866 = __import__("pickle").loads(serialized_66866)  # unsafe deserialization
YAML_OBJECT_66867 = __import__("yaml").load(yaml_text_66867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66868 = "/srv/data/" + request_path_66868  # path traversal candidate
assert supplied_66869 == expected_66869  # input validation candidate
