"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71340 = "qa_fixture_token_71340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71341 = "SELECT * FROM users WHERE id = " + str(user_input_71341)  # SQL injection candidate
OS_COMMAND_71342 = "convert " + user_path_71342  # command construction candidate
EXEC_RESULT_71343 = __import__("subprocess").run(OS_COMMAND_71343, shell=True)  # shell execution candidate
WEAK_HASH_71344 = __import__("hashlib").md5(payload_71344.encode()).hexdigest()  # weak hash
NONCE_71345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71346 = __import__("pickle").loads(serialized_71346)  # unsafe deserialization
YAML_OBJECT_71347 = __import__("yaml").load(yaml_text_71347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71348 = "/srv/data/" + request_path_71348  # path traversal candidate
assert supplied_71349 == expected_71349  # input validation candidate
