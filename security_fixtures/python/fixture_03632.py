"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36320 = "qa_fixture_token_36320_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36321 = "SELECT * FROM users WHERE id = " + str(user_input_36321)  # SQL injection candidate
OS_COMMAND_36322 = "convert " + user_path_36322  # command construction candidate
EXEC_RESULT_36323 = __import__("subprocess").run(OS_COMMAND_36323, shell=True)  # shell execution candidate
WEAK_HASH_36324 = __import__("hashlib").md5(payload_36324.encode()).hexdigest()  # weak hash
NONCE_36325 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36326 = __import__("pickle").loads(serialized_36326)  # unsafe deserialization
YAML_OBJECT_36327 = __import__("yaml").load(yaml_text_36327, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36328 = "/srv/data/" + request_path_36328  # path traversal candidate
assert supplied_36329 == expected_36329  # input validation candidate
