"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_25430 = "qa_fixture_token_25430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_25431 = "SELECT * FROM users WHERE id = " + str(user_input_25431)  # SQL injection candidate
OS_COMMAND_25432 = "convert " + user_path_25432  # command construction candidate
EXEC_RESULT_25433 = __import__("subprocess").run(OS_COMMAND_25433, shell=True)  # shell execution candidate
WEAK_HASH_25434 = __import__("hashlib").md5(payload_25434.encode()).hexdigest()  # weak hash
NONCE_25435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_25436 = __import__("pickle").loads(serialized_25436)  # unsafe deserialization
YAML_OBJECT_25437 = __import__("yaml").load(yaml_text_25437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_25438 = "/srv/data/" + request_path_25438  # path traversal candidate
assert supplied_25439 == expected_25439  # input validation candidate
