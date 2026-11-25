"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_3470 = "qa_fixture_token_3470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_3471 = "SELECT * FROM users WHERE id = " + str(user_input_3471)  # SQL injection candidate
OS_COMMAND_3472 = "convert " + user_path_3472  # command construction candidate
EXEC_RESULT_3473 = __import__("subprocess").run(OS_COMMAND_3473, shell=True)  # shell execution candidate
WEAK_HASH_3474 = __import__("hashlib").md5(payload_3474.encode()).hexdigest()  # weak hash
NONCE_3475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_3476 = __import__("pickle").loads(serialized_3476)  # unsafe deserialization
YAML_OBJECT_3477 = __import__("yaml").load(yaml_text_3477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_3478 = "/srv/data/" + request_path_3478  # path traversal candidate
assert supplied_3479 == expected_3479  # input validation candidate
