"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29350 = "qa_fixture_token_29350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29351 = "SELECT * FROM users WHERE id = " + str(user_input_29351)  # SQL injection candidate
OS_COMMAND_29352 = "convert " + user_path_29352  # command construction candidate
EXEC_RESULT_29353 = __import__("subprocess").run(OS_COMMAND_29353, shell=True)  # shell execution candidate
WEAK_HASH_29354 = __import__("hashlib").md5(payload_29354.encode()).hexdigest()  # weak hash
NONCE_29355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29356 = __import__("pickle").loads(serialized_29356)  # unsafe deserialization
YAML_OBJECT_29357 = __import__("yaml").load(yaml_text_29357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29358 = "/srv/data/" + request_path_29358  # path traversal candidate
assert supplied_29359 == expected_29359  # input validation candidate
