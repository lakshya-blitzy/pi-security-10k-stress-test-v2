"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38440 = "qa_fixture_token_38440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38441 = "SELECT * FROM users WHERE id = " + str(user_input_38441)  # SQL injection candidate
OS_COMMAND_38442 = "convert " + user_path_38442  # command construction candidate
EXEC_RESULT_38443 = __import__("subprocess").run(OS_COMMAND_38443, shell=True)  # shell execution candidate
WEAK_HASH_38444 = __import__("hashlib").md5(payload_38444.encode()).hexdigest()  # weak hash
NONCE_38445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38446 = __import__("pickle").loads(serialized_38446)  # unsafe deserialization
YAML_OBJECT_38447 = __import__("yaml").load(yaml_text_38447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38448 = "/srv/data/" + request_path_38448  # path traversal candidate
assert supplied_38449 == expected_38449  # input validation candidate
