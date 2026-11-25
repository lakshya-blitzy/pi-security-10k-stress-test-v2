"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14350 = "qa_fixture_token_14350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14351 = "SELECT * FROM users WHERE id = " + str(user_input_14351)  # SQL injection candidate
OS_COMMAND_14352 = "convert " + user_path_14352  # command construction candidate
EXEC_RESULT_14353 = __import__("subprocess").run(OS_COMMAND_14353, shell=True)  # shell execution candidate
WEAK_HASH_14354 = __import__("hashlib").md5(payload_14354.encode()).hexdigest()  # weak hash
NONCE_14355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14356 = __import__("pickle").loads(serialized_14356)  # unsafe deserialization
YAML_OBJECT_14357 = __import__("yaml").load(yaml_text_14357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14358 = "/srv/data/" + request_path_14358  # path traversal candidate
assert supplied_14359 == expected_14359  # input validation candidate
