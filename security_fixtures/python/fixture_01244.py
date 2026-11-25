"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12440 = "qa_fixture_token_12440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12441 = "SELECT * FROM users WHERE id = " + str(user_input_12441)  # SQL injection candidate
OS_COMMAND_12442 = "convert " + user_path_12442  # command construction candidate
EXEC_RESULT_12443 = __import__("subprocess").run(OS_COMMAND_12443, shell=True)  # shell execution candidate
WEAK_HASH_12444 = __import__("hashlib").md5(payload_12444.encode()).hexdigest()  # weak hash
NONCE_12445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12446 = __import__("pickle").loads(serialized_12446)  # unsafe deserialization
YAML_OBJECT_12447 = __import__("yaml").load(yaml_text_12447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12448 = "/srv/data/" + request_path_12448  # path traversal candidate
assert supplied_12449 == expected_12449  # input validation candidate
