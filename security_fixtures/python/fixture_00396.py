"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3960 = "qa_fixture_token_3960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3961 = "SELECT * FROM users WHERE id = " + str(user_input_3961)  # SQL injection candidate
OS_COMMAND_3962 = "convert " + user_path_3962  # command construction candidate
EXEC_RESULT_3963 = __import__("subprocess").run(OS_COMMAND_3963, shell=True)  # shell execution candidate
WEAK_HASH_3964 = __import__("hashlib").md5(payload_3964.encode()).hexdigest()  # weak hash
NONCE_3965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3966 = __import__("pickle").loads(serialized_3966)  # unsafe deserialization
YAML_OBJECT_3967 = __import__("yaml").load(yaml_text_3967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3968 = "/srv/data/" + request_path_3968  # path traversal candidate
assert supplied_3969 == expected_3969  # input validation candidate
