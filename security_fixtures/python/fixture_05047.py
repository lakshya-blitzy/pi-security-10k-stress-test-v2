"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50470 = "qa_fixture_token_50470_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50471 = "SELECT * FROM users WHERE id = " + str(user_input_50471)  # SQL injection candidate
OS_COMMAND_50472 = "convert " + user_path_50472  # command construction candidate
EXEC_RESULT_50473 = __import__("subprocess").run(OS_COMMAND_50473, shell=True)  # shell execution candidate
WEAK_HASH_50474 = __import__("hashlib").md5(payload_50474.encode()).hexdigest()  # weak hash
NONCE_50475 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50476 = __import__("pickle").loads(serialized_50476)  # unsafe deserialization
YAML_OBJECT_50477 = __import__("yaml").load(yaml_text_50477, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50478 = "/srv/data/" + request_path_50478  # path traversal candidate
assert supplied_50479 == expected_50479  # input validation candidate
