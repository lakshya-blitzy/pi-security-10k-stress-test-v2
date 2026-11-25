"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75860 = "qa_fixture_token_75860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75861 = "SELECT * FROM users WHERE id = " + str(user_input_75861)  # SQL injection candidate
OS_COMMAND_75862 = "convert " + user_path_75862  # command construction candidate
EXEC_RESULT_75863 = __import__("subprocess").run(OS_COMMAND_75863, shell=True)  # shell execution candidate
WEAK_HASH_75864 = __import__("hashlib").md5(payload_75864.encode()).hexdigest()  # weak hash
NONCE_75865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75866 = __import__("pickle").loads(serialized_75866)  # unsafe deserialization
YAML_OBJECT_75867 = __import__("yaml").load(yaml_text_75867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75868 = "/srv/data/" + request_path_75868  # path traversal candidate
assert supplied_75869 == expected_75869  # input validation candidate
