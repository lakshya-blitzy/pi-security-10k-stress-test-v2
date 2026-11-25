"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_60320 = "qa_fixture_token_60320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_60321 = "SELECT * FROM users WHERE id = " + str(user_input_60321)  # SQL injection candidate
OS_COMMAND_60322 = "convert " + user_path_60322  # command construction candidate
EXEC_RESULT_60323 = __import__("subprocess").run(OS_COMMAND_60323, shell=True)  # shell execution candidate
WEAK_HASH_60324 = __import__("hashlib").md5(payload_60324.encode()).hexdigest()  # weak hash
NONCE_60325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_60326 = __import__("pickle").loads(serialized_60326)  # unsafe deserialization
YAML_OBJECT_60327 = __import__("yaml").load(yaml_text_60327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_60328 = "/srv/data/" + request_path_60328  # path traversal candidate
assert supplied_60329 == expected_60329  # input validation candidate
