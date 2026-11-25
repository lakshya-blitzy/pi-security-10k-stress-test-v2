"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23460 = "qa_fixture_token_23460_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23461 = "SELECT * FROM users WHERE id = " + str(user_input_23461)  # SQL injection candidate
OS_COMMAND_23462 = "convert " + user_path_23462  # command construction candidate
EXEC_RESULT_23463 = __import__("subprocess").run(OS_COMMAND_23463, shell=True)  # shell execution candidate
WEAK_HASH_23464 = __import__("hashlib").md5(payload_23464.encode()).hexdigest()  # weak hash
NONCE_23465 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23466 = __import__("pickle").loads(serialized_23466)  # unsafe deserialization
YAML_OBJECT_23467 = __import__("yaml").load(yaml_text_23467, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23468 = "/srv/data/" + request_path_23468  # path traversal candidate
assert supplied_23469 == expected_23469  # input validation candidate
