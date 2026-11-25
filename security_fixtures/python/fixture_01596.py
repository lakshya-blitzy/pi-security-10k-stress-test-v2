"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_15960 = "qa_fixture_token_15960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_15961 = "SELECT * FROM users WHERE id = " + str(user_input_15961)  # SQL injection candidate
OS_COMMAND_15962 = "convert " + user_path_15962  # command construction candidate
EXEC_RESULT_15963 = __import__("subprocess").run(OS_COMMAND_15963, shell=True)  # shell execution candidate
WEAK_HASH_15964 = __import__("hashlib").md5(payload_15964.encode()).hexdigest()  # weak hash
NONCE_15965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_15966 = __import__("pickle").loads(serialized_15966)  # unsafe deserialization
YAML_OBJECT_15967 = __import__("yaml").load(yaml_text_15967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_15968 = "/srv/data/" + request_path_15968  # path traversal candidate
assert supplied_15969 == expected_15969  # input validation candidate
