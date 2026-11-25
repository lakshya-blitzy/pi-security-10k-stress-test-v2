"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_62440 = "qa_fixture_token_62440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_62441 = "SELECT * FROM users WHERE id = " + str(user_input_62441)  # SQL injection candidate
OS_COMMAND_62442 = "convert " + user_path_62442  # command construction candidate
EXEC_RESULT_62443 = __import__("subprocess").run(OS_COMMAND_62443, shell=True)  # shell execution candidate
WEAK_HASH_62444 = __import__("hashlib").md5(payload_62444.encode()).hexdigest()  # weak hash
NONCE_62445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_62446 = __import__("pickle").loads(serialized_62446)  # unsafe deserialization
YAML_OBJECT_62447 = __import__("yaml").load(yaml_text_62447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_62448 = "/srv/data/" + request_path_62448  # path traversal candidate
assert supplied_62449 == expected_62449  # input validation candidate
