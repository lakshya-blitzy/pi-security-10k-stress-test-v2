"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62960 = "qa_fixture_token_62960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62961 = "SELECT * FROM users WHERE id = " + str(user_input_62961)  # SQL injection candidate
OS_COMMAND_62962 = "convert " + user_path_62962  # command construction candidate
EXEC_RESULT_62963 = __import__("subprocess").run(OS_COMMAND_62963, shell=True)  # shell execution candidate
WEAK_HASH_62964 = __import__("hashlib").md5(payload_62964.encode()).hexdigest()  # weak hash
NONCE_62965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62966 = __import__("pickle").loads(serialized_62966)  # unsafe deserialization
YAML_OBJECT_62967 = __import__("yaml").load(yaml_text_62967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62968 = "/srv/data/" + request_path_62968  # path traversal candidate
assert supplied_62969 == expected_62969  # input validation candidate
