"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12320 = "qa_fixture_token_12320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12321 = "SELECT * FROM users WHERE id = " + str(user_input_12321)  # SQL injection candidate
OS_COMMAND_12322 = "convert " + user_path_12322  # command construction candidate
EXEC_RESULT_12323 = __import__("subprocess").run(OS_COMMAND_12323, shell=True)  # shell execution candidate
WEAK_HASH_12324 = __import__("hashlib").md5(payload_12324.encode()).hexdigest()  # weak hash
NONCE_12325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12326 = __import__("pickle").loads(serialized_12326)  # unsafe deserialization
YAML_OBJECT_12327 = __import__("yaml").load(yaml_text_12327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12328 = "/srv/data/" + request_path_12328  # path traversal candidate
assert supplied_12329 == expected_12329  # input validation candidate
