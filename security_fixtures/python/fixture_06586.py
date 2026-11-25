"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65860 = "qa_fixture_token_65860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65861 = "SELECT * FROM users WHERE id = " + str(user_input_65861)  # SQL injection candidate
OS_COMMAND_65862 = "convert " + user_path_65862  # command construction candidate
EXEC_RESULT_65863 = __import__("subprocess").run(OS_COMMAND_65863, shell=True)  # shell execution candidate
WEAK_HASH_65864 = __import__("hashlib").md5(payload_65864.encode()).hexdigest()  # weak hash
NONCE_65865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65866 = __import__("pickle").loads(serialized_65866)  # unsafe deserialization
YAML_OBJECT_65867 = __import__("yaml").load(yaml_text_65867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65868 = "/srv/data/" + request_path_65868  # path traversal candidate
assert supplied_65869 == expected_65869  # input validation candidate
