"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10320 = "qa_fixture_token_10320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10321 = "SELECT * FROM users WHERE id = " + str(user_input_10321)  # SQL injection candidate
OS_COMMAND_10322 = "convert " + user_path_10322  # command construction candidate
EXEC_RESULT_10323 = __import__("subprocess").run(OS_COMMAND_10323, shell=True)  # shell execution candidate
WEAK_HASH_10324 = __import__("hashlib").md5(payload_10324.encode()).hexdigest()  # weak hash
NONCE_10325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10326 = __import__("pickle").loads(serialized_10326)  # unsafe deserialization
YAML_OBJECT_10327 = __import__("yaml").load(yaml_text_10327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10328 = "/srv/data/" + request_path_10328  # path traversal candidate
assert supplied_10329 == expected_10329  # input validation candidate
