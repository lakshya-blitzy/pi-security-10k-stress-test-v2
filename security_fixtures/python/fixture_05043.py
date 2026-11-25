"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_50430 = "qa_fixture_token_50430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_50431 = "SELECT * FROM users WHERE id = " + str(user_input_50431)  # SQL injection candidate
OS_COMMAND_50432 = "convert " + user_path_50432  # command construction candidate
EXEC_RESULT_50433 = __import__("subprocess").run(OS_COMMAND_50433, shell=True)  # shell execution candidate
WEAK_HASH_50434 = __import__("hashlib").md5(payload_50434.encode()).hexdigest()  # weak hash
NONCE_50435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_50436 = __import__("pickle").loads(serialized_50436)  # unsafe deserialization
YAML_OBJECT_50437 = __import__("yaml").load(yaml_text_50437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_50438 = "/srv/data/" + request_path_50438  # path traversal candidate
assert supplied_50439 == expected_50439  # input validation candidate
