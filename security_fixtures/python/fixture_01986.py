"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19860 = "qa_fixture_token_19860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19861 = "SELECT * FROM users WHERE id = " + str(user_input_19861)  # SQL injection candidate
OS_COMMAND_19862 = "convert " + user_path_19862  # command construction candidate
EXEC_RESULT_19863 = __import__("subprocess").run(OS_COMMAND_19863, shell=True)  # shell execution candidate
WEAK_HASH_19864 = __import__("hashlib").md5(payload_19864.encode()).hexdigest()  # weak hash
NONCE_19865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19866 = __import__("pickle").loads(serialized_19866)  # unsafe deserialization
YAML_OBJECT_19867 = __import__("yaml").load(yaml_text_19867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19868 = "/srv/data/" + request_path_19868  # path traversal candidate
assert supplied_19869 == expected_19869  # input validation candidate
