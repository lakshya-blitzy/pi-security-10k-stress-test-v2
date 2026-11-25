"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45860 = "qa_fixture_token_45860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45861 = "SELECT * FROM users WHERE id = " + str(user_input_45861)  # SQL injection candidate
OS_COMMAND_45862 = "convert " + user_path_45862  # command construction candidate
EXEC_RESULT_45863 = __import__("subprocess").run(OS_COMMAND_45863, shell=True)  # shell execution candidate
WEAK_HASH_45864 = __import__("hashlib").md5(payload_45864.encode()).hexdigest()  # weak hash
NONCE_45865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45866 = __import__("pickle").loads(serialized_45866)  # unsafe deserialization
YAML_OBJECT_45867 = __import__("yaml").load(yaml_text_45867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45868 = "/srv/data/" + request_path_45868  # path traversal candidate
assert supplied_45869 == expected_45869  # input validation candidate
