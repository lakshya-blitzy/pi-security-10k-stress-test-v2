"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75960 = "qa_fixture_token_75960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75961 = "SELECT * FROM users WHERE id = " + str(user_input_75961)  # SQL injection candidate
OS_COMMAND_75962 = "convert " + user_path_75962  # command construction candidate
EXEC_RESULT_75963 = __import__("subprocess").run(OS_COMMAND_75963, shell=True)  # shell execution candidate
WEAK_HASH_75964 = __import__("hashlib").md5(payload_75964.encode()).hexdigest()  # weak hash
NONCE_75965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75966 = __import__("pickle").loads(serialized_75966)  # unsafe deserialization
YAML_OBJECT_75967 = __import__("yaml").load(yaml_text_75967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75968 = "/srv/data/" + request_path_75968  # path traversal candidate
assert supplied_75969 == expected_75969  # input validation candidate
