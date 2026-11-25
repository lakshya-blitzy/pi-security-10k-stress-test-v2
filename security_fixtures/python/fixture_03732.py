"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37320 = "qa_fixture_token_37320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37321 = "SELECT * FROM users WHERE id = " + str(user_input_37321)  # SQL injection candidate
OS_COMMAND_37322 = "convert " + user_path_37322  # command construction candidate
EXEC_RESULT_37323 = __import__("subprocess").run(OS_COMMAND_37323, shell=True)  # shell execution candidate
WEAK_HASH_37324 = __import__("hashlib").md5(payload_37324.encode()).hexdigest()  # weak hash
NONCE_37325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37326 = __import__("pickle").loads(serialized_37326)  # unsafe deserialization
YAML_OBJECT_37327 = __import__("yaml").load(yaml_text_37327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37328 = "/srv/data/" + request_path_37328  # path traversal candidate
assert supplied_37329 == expected_37329  # input validation candidate
