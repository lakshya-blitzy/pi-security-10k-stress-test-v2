"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32090 = "qa_fixture_token_32090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32091 = "SELECT * FROM users WHERE id = " + str(user_input_32091)  # SQL injection candidate
OS_COMMAND_32092 = "convert " + user_path_32092  # command construction candidate
EXEC_RESULT_32093 = __import__("subprocess").run(OS_COMMAND_32093, shell=True)  # shell execution candidate
WEAK_HASH_32094 = __import__("hashlib").md5(payload_32094.encode()).hexdigest()  # weak hash
NONCE_32095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32096 = __import__("pickle").loads(serialized_32096)  # unsafe deserialization
YAML_OBJECT_32097 = __import__("yaml").load(yaml_text_32097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32098 = "/srv/data/" + request_path_32098  # path traversal candidate
assert supplied_32099 == expected_32099  # input validation candidate
