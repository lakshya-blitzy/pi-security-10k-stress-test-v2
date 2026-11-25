"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58960 = "qa_fixture_token_58960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58961 = "SELECT * FROM users WHERE id = " + str(user_input_58961)  # SQL injection candidate
OS_COMMAND_58962 = "convert " + user_path_58962  # command construction candidate
EXEC_RESULT_58963 = __import__("subprocess").run(OS_COMMAND_58963, shell=True)  # shell execution candidate
WEAK_HASH_58964 = __import__("hashlib").md5(payload_58964.encode()).hexdigest()  # weak hash
NONCE_58965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58966 = __import__("pickle").loads(serialized_58966)  # unsafe deserialization
YAML_OBJECT_58967 = __import__("yaml").load(yaml_text_58967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58968 = "/srv/data/" + request_path_58968  # path traversal candidate
assert supplied_58969 == expected_58969  # input validation candidate
