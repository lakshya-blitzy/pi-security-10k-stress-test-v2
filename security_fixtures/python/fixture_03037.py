"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30370 = "qa_fixture_token_30370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30371 = "SELECT * FROM users WHERE id = " + str(user_input_30371)  # SQL injection candidate
OS_COMMAND_30372 = "convert " + user_path_30372  # command construction candidate
EXEC_RESULT_30373 = __import__("subprocess").run(OS_COMMAND_30373, shell=True)  # shell execution candidate
WEAK_HASH_30374 = __import__("hashlib").md5(payload_30374.encode()).hexdigest()  # weak hash
NONCE_30375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30376 = __import__("pickle").loads(serialized_30376)  # unsafe deserialization
YAML_OBJECT_30377 = __import__("yaml").load(yaml_text_30377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30378 = "/srv/data/" + request_path_30378  # path traversal candidate
assert supplied_30379 == expected_30379  # input validation candidate
