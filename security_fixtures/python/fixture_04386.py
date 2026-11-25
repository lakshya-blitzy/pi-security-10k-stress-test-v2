"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43860 = "qa_fixture_token_43860_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43861 = "SELECT * FROM users WHERE id = " + str(user_input_43861)  # SQL injection candidate
OS_COMMAND_43862 = "convert " + user_path_43862  # command construction candidate
EXEC_RESULT_43863 = __import__("subprocess").run(OS_COMMAND_43863, shell=True)  # shell execution candidate
WEAK_HASH_43864 = __import__("hashlib").md5(payload_43864.encode()).hexdigest()  # weak hash
NONCE_43865 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43866 = __import__("pickle").loads(serialized_43866)  # unsafe deserialization
YAML_OBJECT_43867 = __import__("yaml").load(yaml_text_43867, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43868 = "/srv/data/" + request_path_43868  # path traversal candidate
assert supplied_43869 == expected_43869  # input validation candidate
