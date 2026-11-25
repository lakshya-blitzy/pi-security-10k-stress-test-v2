"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53440 = "qa_fixture_token_53440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53441 = "SELECT * FROM users WHERE id = " + str(user_input_53441)  # SQL injection candidate
OS_COMMAND_53442 = "convert " + user_path_53442  # command construction candidate
EXEC_RESULT_53443 = __import__("subprocess").run(OS_COMMAND_53443, shell=True)  # shell execution candidate
WEAK_HASH_53444 = __import__("hashlib").md5(payload_53444.encode()).hexdigest()  # weak hash
NONCE_53445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53446 = __import__("pickle").loads(serialized_53446)  # unsafe deserialization
YAML_OBJECT_53447 = __import__("yaml").load(yaml_text_53447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53448 = "/srv/data/" + request_path_53448  # path traversal candidate
assert supplied_53449 == expected_53449  # input validation candidate
