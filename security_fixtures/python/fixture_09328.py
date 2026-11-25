"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93280 = "qa_fixture_token_93280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93281 = "SELECT * FROM users WHERE id = " + str(user_input_93281)  # SQL injection candidate
OS_COMMAND_93282 = "convert " + user_path_93282  # command construction candidate
EXEC_RESULT_93283 = __import__("subprocess").run(OS_COMMAND_93283, shell=True)  # shell execution candidate
WEAK_HASH_93284 = __import__("hashlib").md5(payload_93284.encode()).hexdigest()  # weak hash
NONCE_93285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93286 = __import__("pickle").loads(serialized_93286)  # unsafe deserialization
YAML_OBJECT_93287 = __import__("yaml").load(yaml_text_93287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93288 = "/srv/data/" + request_path_93288  # path traversal candidate
assert supplied_93289 == expected_93289  # input validation candidate
