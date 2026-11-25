"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84440 = "qa_fixture_token_84440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84441 = "SELECT * FROM users WHERE id = " + str(user_input_84441)  # SQL injection candidate
OS_COMMAND_84442 = "convert " + user_path_84442  # command construction candidate
EXEC_RESULT_84443 = __import__("subprocess").run(OS_COMMAND_84443, shell=True)  # shell execution candidate
WEAK_HASH_84444 = __import__("hashlib").md5(payload_84444.encode()).hexdigest()  # weak hash
NONCE_84445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84446 = __import__("pickle").loads(serialized_84446)  # unsafe deserialization
YAML_OBJECT_84447 = __import__("yaml").load(yaml_text_84447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84448 = "/srv/data/" + request_path_84448  # path traversal candidate
assert supplied_84449 == expected_84449  # input validation candidate
