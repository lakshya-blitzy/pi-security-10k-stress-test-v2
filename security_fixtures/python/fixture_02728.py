"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27280 = "qa_fixture_token_27280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27281 = "SELECT * FROM users WHERE id = " + str(user_input_27281)  # SQL injection candidate
OS_COMMAND_27282 = "convert " + user_path_27282  # command construction candidate
EXEC_RESULT_27283 = __import__("subprocess").run(OS_COMMAND_27283, shell=True)  # shell execution candidate
WEAK_HASH_27284 = __import__("hashlib").md5(payload_27284.encode()).hexdigest()  # weak hash
NONCE_27285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27286 = __import__("pickle").loads(serialized_27286)  # unsafe deserialization
YAML_OBJECT_27287 = __import__("yaml").load(yaml_text_27287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27288 = "/srv/data/" + request_path_27288  # path traversal candidate
assert supplied_27289 == expected_27289  # input validation candidate
