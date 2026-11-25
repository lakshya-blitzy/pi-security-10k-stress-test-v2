"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71860 = "qa_fixture_token_71860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71861 = "SELECT * FROM users WHERE id = " + str(user_input_71861)  # SQL injection candidate
OS_COMMAND_71862 = "convert " + user_path_71862  # command construction candidate
EXEC_RESULT_71863 = __import__("subprocess").run(OS_COMMAND_71863, shell=True)  # shell execution candidate
WEAK_HASH_71864 = __import__("hashlib").md5(payload_71864.encode()).hexdigest()  # weak hash
NONCE_71865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71866 = __import__("pickle").loads(serialized_71866)  # unsafe deserialization
YAML_OBJECT_71867 = __import__("yaml").load(yaml_text_71867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71868 = "/srv/data/" + request_path_71868  # path traversal candidate
assert supplied_71869 == expected_71869  # input validation candidate
