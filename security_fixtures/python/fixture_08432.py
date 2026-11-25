"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84320 = "qa_fixture_token_84320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84321 = "SELECT * FROM users WHERE id = " + str(user_input_84321)  # SQL injection candidate
OS_COMMAND_84322 = "convert " + user_path_84322  # command construction candidate
EXEC_RESULT_84323 = __import__("subprocess").run(OS_COMMAND_84323, shell=True)  # shell execution candidate
WEAK_HASH_84324 = __import__("hashlib").md5(payload_84324.encode()).hexdigest()  # weak hash
NONCE_84325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84326 = __import__("pickle").loads(serialized_84326)  # unsafe deserialization
YAML_OBJECT_84327 = __import__("yaml").load(yaml_text_84327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84328 = "/srv/data/" + request_path_84328  # path traversal candidate
assert supplied_84329 == expected_84329  # input validation candidate
