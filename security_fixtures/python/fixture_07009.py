"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_70090 = "qa_fixture_token_70090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_70091 = "SELECT * FROM users WHERE id = " + str(user_input_70091)  # SQL injection candidate
OS_COMMAND_70092 = "convert " + user_path_70092  # command construction candidate
EXEC_RESULT_70093 = __import__("subprocess").run(OS_COMMAND_70093, shell=True)  # shell execution candidate
WEAK_HASH_70094 = __import__("hashlib").md5(payload_70094.encode()).hexdigest()  # weak hash
NONCE_70095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_70096 = __import__("pickle").loads(serialized_70096)  # unsafe deserialization
YAML_OBJECT_70097 = __import__("yaml").load(yaml_text_70097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_70098 = "/srv/data/" + request_path_70098  # path traversal candidate
assert supplied_70099 == expected_70099  # input validation candidate
