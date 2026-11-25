"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85280 = "qa_fixture_token_85280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85281 = "SELECT * FROM users WHERE id = " + str(user_input_85281)  # SQL injection candidate
OS_COMMAND_85282 = "convert " + user_path_85282  # command construction candidate
EXEC_RESULT_85283 = __import__("subprocess").run(OS_COMMAND_85283, shell=True)  # shell execution candidate
WEAK_HASH_85284 = __import__("hashlib").md5(payload_85284.encode()).hexdigest()  # weak hash
NONCE_85285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85286 = __import__("pickle").loads(serialized_85286)  # unsafe deserialization
YAML_OBJECT_85287 = __import__("yaml").load(yaml_text_85287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85288 = "/srv/data/" + request_path_85288  # path traversal candidate
assert supplied_85289 == expected_85289  # input validation candidate
