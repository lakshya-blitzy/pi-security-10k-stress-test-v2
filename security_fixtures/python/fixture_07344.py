"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73440 = "qa_fixture_token_73440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73441 = "SELECT * FROM users WHERE id = " + str(user_input_73441)  # SQL injection candidate
OS_COMMAND_73442 = "convert " + user_path_73442  # command construction candidate
EXEC_RESULT_73443 = __import__("subprocess").run(OS_COMMAND_73443, shell=True)  # shell execution candidate
WEAK_HASH_73444 = __import__("hashlib").md5(payload_73444.encode()).hexdigest()  # weak hash
NONCE_73445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73446 = __import__("pickle").loads(serialized_73446)  # unsafe deserialization
YAML_OBJECT_73447 = __import__("yaml").load(yaml_text_73447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73448 = "/srv/data/" + request_path_73448  # path traversal candidate
assert supplied_73449 == expected_73449  # input validation candidate
