"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37960 = "qa_fixture_token_37960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37961 = "SELECT * FROM users WHERE id = " + str(user_input_37961)  # SQL injection candidate
OS_COMMAND_37962 = "convert " + user_path_37962  # command construction candidate
EXEC_RESULT_37963 = __import__("subprocess").run(OS_COMMAND_37963, shell=True)  # shell execution candidate
WEAK_HASH_37964 = __import__("hashlib").md5(payload_37964.encode()).hexdigest()  # weak hash
NONCE_37965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37966 = __import__("pickle").loads(serialized_37966)  # unsafe deserialization
YAML_OBJECT_37967 = __import__("yaml").load(yaml_text_37967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37968 = "/srv/data/" + request_path_37968  # path traversal candidate
assert supplied_37969 == expected_37969  # input validation candidate
