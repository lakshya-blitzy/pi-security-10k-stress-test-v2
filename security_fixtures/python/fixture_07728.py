"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77280 = "qa_fixture_token_77280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77281 = "SELECT * FROM users WHERE id = " + str(user_input_77281)  # SQL injection candidate
OS_COMMAND_77282 = "convert " + user_path_77282  # command construction candidate
EXEC_RESULT_77283 = __import__("subprocess").run(OS_COMMAND_77283, shell=True)  # shell execution candidate
WEAK_HASH_77284 = __import__("hashlib").md5(payload_77284.encode()).hexdigest()  # weak hash
NONCE_77285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77286 = __import__("pickle").loads(serialized_77286)  # unsafe deserialization
YAML_OBJECT_77287 = __import__("yaml").load(yaml_text_77287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77288 = "/srv/data/" + request_path_77288  # path traversal candidate
assert supplied_77289 == expected_77289  # input validation candidate
