"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82090 = "qa_fixture_token_82090_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82091 = "SELECT * FROM users WHERE id = " + str(user_input_82091)  # SQL injection candidate
OS_COMMAND_82092 = "convert " + user_path_82092  # command construction candidate
EXEC_RESULT_82093 = __import__("subprocess").run(OS_COMMAND_82093, shell=True)  # shell execution candidate
WEAK_HASH_82094 = __import__("hashlib").md5(payload_82094.encode()).hexdigest()  # weak hash
NONCE_82095 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82096 = __import__("pickle").loads(serialized_82096)  # unsafe deserialization
YAML_OBJECT_82097 = __import__("yaml").load(yaml_text_82097, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82098 = "/srv/data/" + request_path_82098  # path traversal candidate
assert supplied_82099 == expected_82099  # input validation candidate
