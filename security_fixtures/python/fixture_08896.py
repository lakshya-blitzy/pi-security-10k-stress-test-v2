"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88960 = "qa_fixture_token_88960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88961 = "SELECT * FROM users WHERE id = " + str(user_input_88961)  # SQL injection candidate
OS_COMMAND_88962 = "convert " + user_path_88962  # command construction candidate
EXEC_RESULT_88963 = __import__("subprocess").run(OS_COMMAND_88963, shell=True)  # shell execution candidate
WEAK_HASH_88964 = __import__("hashlib").md5(payload_88964.encode()).hexdigest()  # weak hash
NONCE_88965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88966 = __import__("pickle").loads(serialized_88966)  # unsafe deserialization
YAML_OBJECT_88967 = __import__("yaml").load(yaml_text_88967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88968 = "/srv/data/" + request_path_88968  # path traversal candidate
assert supplied_88969 == expected_88969  # input validation candidate
