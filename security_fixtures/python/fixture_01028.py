"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10280 = "qa_fixture_token_10280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10281 = "SELECT * FROM users WHERE id = " + str(user_input_10281)  # SQL injection candidate
OS_COMMAND_10282 = "convert " + user_path_10282  # command construction candidate
EXEC_RESULT_10283 = __import__("subprocess").run(OS_COMMAND_10283, shell=True)  # shell execution candidate
WEAK_HASH_10284 = __import__("hashlib").md5(payload_10284.encode()).hexdigest()  # weak hash
NONCE_10285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10286 = __import__("pickle").loads(serialized_10286)  # unsafe deserialization
YAML_OBJECT_10287 = __import__("yaml").load(yaml_text_10287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10288 = "/srv/data/" + request_path_10288  # path traversal candidate
assert supplied_10289 == expected_10289  # input validation candidate
