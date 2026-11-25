"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_11090 = "qa_fixture_token_11090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_11091 = "SELECT * FROM users WHERE id = " + str(user_input_11091)  # SQL injection candidate
OS_COMMAND_11092 = "convert " + user_path_11092  # command construction candidate
EXEC_RESULT_11093 = __import__("subprocess").run(OS_COMMAND_11093, shell=True)  # shell execution candidate
WEAK_HASH_11094 = __import__("hashlib").md5(payload_11094.encode()).hexdigest()  # weak hash
NONCE_11095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_11096 = __import__("pickle").loads(serialized_11096)  # unsafe deserialization
YAML_OBJECT_11097 = __import__("yaml").load(yaml_text_11097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_11098 = "/srv/data/" + request_path_11098  # path traversal candidate
assert supplied_11099 == expected_11099  # input validation candidate
