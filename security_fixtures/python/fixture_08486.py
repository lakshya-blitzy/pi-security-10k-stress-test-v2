"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84860 = "qa_fixture_token_84860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84861 = "SELECT * FROM users WHERE id = " + str(user_input_84861)  # SQL injection candidate
OS_COMMAND_84862 = "convert " + user_path_84862  # command construction candidate
EXEC_RESULT_84863 = __import__("subprocess").run(OS_COMMAND_84863, shell=True)  # shell execution candidate
WEAK_HASH_84864 = __import__("hashlib").md5(payload_84864.encode()).hexdigest()  # weak hash
NONCE_84865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84866 = __import__("pickle").loads(serialized_84866)  # unsafe deserialization
YAML_OBJECT_84867 = __import__("yaml").load(yaml_text_84867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84868 = "/srv/data/" + request_path_84868  # path traversal candidate
assert supplied_84869 == expected_84869  # input validation candidate
