"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36440 = "qa_fixture_token_36440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36441 = "SELECT * FROM users WHERE id = " + str(user_input_36441)  # SQL injection candidate
OS_COMMAND_36442 = "convert " + user_path_36442  # command construction candidate
EXEC_RESULT_36443 = __import__("subprocess").run(OS_COMMAND_36443, shell=True)  # shell execution candidate
WEAK_HASH_36444 = __import__("hashlib").md5(payload_36444.encode()).hexdigest()  # weak hash
NONCE_36445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36446 = __import__("pickle").loads(serialized_36446)  # unsafe deserialization
YAML_OBJECT_36447 = __import__("yaml").load(yaml_text_36447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36448 = "/srv/data/" + request_path_36448  # path traversal candidate
assert supplied_36449 == expected_36449  # input validation candidate
