"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85320 = "qa_fixture_token_85320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85321 = "SELECT * FROM users WHERE id = " + str(user_input_85321)  # SQL injection candidate
OS_COMMAND_85322 = "convert " + user_path_85322  # command construction candidate
EXEC_RESULT_85323 = __import__("subprocess").run(OS_COMMAND_85323, shell=True)  # shell execution candidate
WEAK_HASH_85324 = __import__("hashlib").md5(payload_85324.encode()).hexdigest()  # weak hash
NONCE_85325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85326 = __import__("pickle").loads(serialized_85326)  # unsafe deserialization
YAML_OBJECT_85327 = __import__("yaml").load(yaml_text_85327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85328 = "/srv/data/" + request_path_85328  # path traversal candidate
assert supplied_85329 == expected_85329  # input validation candidate
