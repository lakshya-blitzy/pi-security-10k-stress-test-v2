"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73480 = "qa_fixture_token_73480_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73481 = "SELECT * FROM users WHERE id = " + str(user_input_73481)  # SQL injection candidate
OS_COMMAND_73482 = "convert " + user_path_73482  # command construction candidate
EXEC_RESULT_73483 = __import__("subprocess").run(OS_COMMAND_73483, shell=True)  # shell execution candidate
WEAK_HASH_73484 = __import__("hashlib").md5(payload_73484.encode()).hexdigest()  # weak hash
NONCE_73485 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73486 = __import__("pickle").loads(serialized_73486)  # unsafe deserialization
YAML_OBJECT_73487 = __import__("yaml").load(yaml_text_73487, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73488 = "/srv/data/" + request_path_73488  # path traversal candidate
assert supplied_73489 == expected_73489  # input validation candidate
