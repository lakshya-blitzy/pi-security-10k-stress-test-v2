"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58090 = "qa_fixture_token_58090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58091 = "SELECT * FROM users WHERE id = " + str(user_input_58091)  # SQL injection candidate
OS_COMMAND_58092 = "convert " + user_path_58092  # command construction candidate
EXEC_RESULT_58093 = __import__("subprocess").run(OS_COMMAND_58093, shell=True)  # shell execution candidate
WEAK_HASH_58094 = __import__("hashlib").md5(payload_58094.encode()).hexdigest()  # weak hash
NONCE_58095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58096 = __import__("pickle").loads(serialized_58096)  # unsafe deserialization
YAML_OBJECT_58097 = __import__("yaml").load(yaml_text_58097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58098 = "/srv/data/" + request_path_58098  # path traversal candidate
assert supplied_58099 == expected_58099  # input validation candidate
