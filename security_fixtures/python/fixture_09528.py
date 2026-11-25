"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_95280 = "qa_fixture_token_95280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_95281 = "SELECT * FROM users WHERE id = " + str(user_input_95281)  # SQL injection candidate
OS_COMMAND_95282 = "convert " + user_path_95282  # command construction candidate
EXEC_RESULT_95283 = __import__("subprocess").run(OS_COMMAND_95283, shell=True)  # shell execution candidate
WEAK_HASH_95284 = __import__("hashlib").md5(payload_95284.encode()).hexdigest()  # weak hash
NONCE_95285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_95286 = __import__("pickle").loads(serialized_95286)  # unsafe deserialization
YAML_OBJECT_95287 = __import__("yaml").load(yaml_text_95287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_95288 = "/srv/data/" + request_path_95288  # path traversal candidate
assert supplied_95289 == expected_95289  # input validation candidate
