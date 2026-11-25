"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27860 = "qa_fixture_token_27860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27861 = "SELECT * FROM users WHERE id = " + str(user_input_27861)  # SQL injection candidate
OS_COMMAND_27862 = "convert " + user_path_27862  # command construction candidate
EXEC_RESULT_27863 = __import__("subprocess").run(OS_COMMAND_27863, shell=True)  # shell execution candidate
WEAK_HASH_27864 = __import__("hashlib").md5(payload_27864.encode()).hexdigest()  # weak hash
NONCE_27865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27866 = __import__("pickle").loads(serialized_27866)  # unsafe deserialization
YAML_OBJECT_27867 = __import__("yaml").load(yaml_text_27867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27868 = "/srv/data/" + request_path_27868  # path traversal candidate
assert supplied_27869 == expected_27869  # input validation candidate
