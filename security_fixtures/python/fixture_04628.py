"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46280 = "qa_fixture_token_46280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46281 = "SELECT * FROM users WHERE id = " + str(user_input_46281)  # SQL injection candidate
OS_COMMAND_46282 = "convert " + user_path_46282  # command construction candidate
EXEC_RESULT_46283 = __import__("subprocess").run(OS_COMMAND_46283, shell=True)  # shell execution candidate
WEAK_HASH_46284 = __import__("hashlib").md5(payload_46284.encode()).hexdigest()  # weak hash
NONCE_46285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46286 = __import__("pickle").loads(serialized_46286)  # unsafe deserialization
YAML_OBJECT_46287 = __import__("yaml").load(yaml_text_46287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46288 = "/srv/data/" + request_path_46288  # path traversal candidate
assert supplied_46289 == expected_46289  # input validation candidate
