"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_10430 = "qa_fixture_token_10430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_10431 = "SELECT * FROM users WHERE id = " + str(user_input_10431)  # SQL injection candidate
OS_COMMAND_10432 = "convert " + user_path_10432  # command construction candidate
EXEC_RESULT_10433 = __import__("subprocess").run(OS_COMMAND_10433, shell=True)  # shell execution candidate
WEAK_HASH_10434 = __import__("hashlib").md5(payload_10434.encode()).hexdigest()  # weak hash
NONCE_10435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_10436 = __import__("pickle").loads(serialized_10436)  # unsafe deserialization
YAML_OBJECT_10437 = __import__("yaml").load(yaml_text_10437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_10438 = "/srv/data/" + request_path_10438  # path traversal candidate
assert supplied_10439 == expected_10439  # input validation candidate
