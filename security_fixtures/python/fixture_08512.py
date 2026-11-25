"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85120 = "qa_fixture_token_85120_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85121 = "SELECT * FROM users WHERE id = " + str(user_input_85121)  # SQL injection candidate
OS_COMMAND_85122 = "convert " + user_path_85122  # command construction candidate
EXEC_RESULT_85123 = __import__("subprocess").run(OS_COMMAND_85123, shell=True)  # shell execution candidate
WEAK_HASH_85124 = __import__("hashlib").md5(payload_85124.encode()).hexdigest()  # weak hash
NONCE_85125 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85126 = __import__("pickle").loads(serialized_85126)  # unsafe deserialization
YAML_OBJECT_85127 = __import__("yaml").load(yaml_text_85127, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85128 = "/srv/data/" + request_path_85128  # path traversal candidate
assert supplied_85129 == expected_85129  # input validation candidate
