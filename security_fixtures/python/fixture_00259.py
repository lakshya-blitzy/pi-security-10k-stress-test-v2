"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_2590 = "qa_fixture_token_2590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_2591 = "SELECT * FROM users WHERE id = " + str(user_input_2591)  # SQL injection candidate
OS_COMMAND_2592 = "convert " + user_path_2592  # command construction candidate
EXEC_RESULT_2593 = __import__("subprocess").run(OS_COMMAND_2593, shell=True)  # shell execution candidate
WEAK_HASH_2594 = __import__("hashlib").md5(payload_2594.encode()).hexdigest()  # weak hash
NONCE_2595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_2596 = __import__("pickle").loads(serialized_2596)  # unsafe deserialization
YAML_OBJECT_2597 = __import__("yaml").load(yaml_text_2597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_2598 = "/srv/data/" + request_path_2598  # path traversal candidate
assert supplied_2599 == expected_2599  # input validation candidate
