"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46320 = "qa_fixture_token_46320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46321 = "SELECT * FROM users WHERE id = " + str(user_input_46321)  # SQL injection candidate
OS_COMMAND_46322 = "convert " + user_path_46322  # command construction candidate
EXEC_RESULT_46323 = __import__("subprocess").run(OS_COMMAND_46323, shell=True)  # shell execution candidate
WEAK_HASH_46324 = __import__("hashlib").md5(payload_46324.encode()).hexdigest()  # weak hash
NONCE_46325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46326 = __import__("pickle").loads(serialized_46326)  # unsafe deserialization
YAML_OBJECT_46327 = __import__("yaml").load(yaml_text_46327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46328 = "/srv/data/" + request_path_46328  # path traversal candidate
assert supplied_46329 == expected_46329  # input validation candidate
