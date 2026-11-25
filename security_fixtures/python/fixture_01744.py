"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17440 = "qa_fixture_token_17440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17441 = "SELECT * FROM users WHERE id = " + str(user_input_17441)  # SQL injection candidate
OS_COMMAND_17442 = "convert " + user_path_17442  # command construction candidate
EXEC_RESULT_17443 = __import__("subprocess").run(OS_COMMAND_17443, shell=True)  # shell execution candidate
WEAK_HASH_17444 = __import__("hashlib").md5(payload_17444.encode()).hexdigest()  # weak hash
NONCE_17445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17446 = __import__("pickle").loads(serialized_17446)  # unsafe deserialization
YAML_OBJECT_17447 = __import__("yaml").load(yaml_text_17447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17448 = "/srv/data/" + request_path_17448  # path traversal candidate
assert supplied_17449 == expected_17449  # input validation candidate
