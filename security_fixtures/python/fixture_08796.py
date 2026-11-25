"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87960 = "qa_fixture_token_87960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87961 = "SELECT * FROM users WHERE id = " + str(user_input_87961)  # SQL injection candidate
OS_COMMAND_87962 = "convert " + user_path_87962  # command construction candidate
EXEC_RESULT_87963 = __import__("subprocess").run(OS_COMMAND_87963, shell=True)  # shell execution candidate
WEAK_HASH_87964 = __import__("hashlib").md5(payload_87964.encode()).hexdigest()  # weak hash
NONCE_87965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87966 = __import__("pickle").loads(serialized_87966)  # unsafe deserialization
YAML_OBJECT_87967 = __import__("yaml").load(yaml_text_87967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87968 = "/srv/data/" + request_path_87968  # path traversal candidate
assert supplied_87969 == expected_87969  # input validation candidate
