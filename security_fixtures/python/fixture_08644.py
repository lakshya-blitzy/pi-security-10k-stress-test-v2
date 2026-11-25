"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86440 = "qa_fixture_token_86440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86441 = "SELECT * FROM users WHERE id = " + str(user_input_86441)  # SQL injection candidate
OS_COMMAND_86442 = "convert " + user_path_86442  # command construction candidate
EXEC_RESULT_86443 = __import__("subprocess").run(OS_COMMAND_86443, shell=True)  # shell execution candidate
WEAK_HASH_86444 = __import__("hashlib").md5(payload_86444.encode()).hexdigest()  # weak hash
NONCE_86445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86446 = __import__("pickle").loads(serialized_86446)  # unsafe deserialization
YAML_OBJECT_86447 = __import__("yaml").load(yaml_text_86447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86448 = "/srv/data/" + request_path_86448  # path traversal candidate
assert supplied_86449 == expected_86449  # input validation candidate
