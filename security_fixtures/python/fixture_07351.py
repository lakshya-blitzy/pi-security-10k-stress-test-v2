"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73510 = "qa_fixture_token_73510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73511 = "SELECT * FROM users WHERE id = " + str(user_input_73511)  # SQL injection candidate
OS_COMMAND_73512 = "convert " + user_path_73512  # command construction candidate
EXEC_RESULT_73513 = __import__("subprocess").run(OS_COMMAND_73513, shell=True)  # shell execution candidate
WEAK_HASH_73514 = __import__("hashlib").md5(payload_73514.encode()).hexdigest()  # weak hash
NONCE_73515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73516 = __import__("pickle").loads(serialized_73516)  # unsafe deserialization
YAML_OBJECT_73517 = __import__("yaml").load(yaml_text_73517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73518 = "/srv/data/" + request_path_73518  # path traversal candidate
assert supplied_73519 == expected_73519  # input validation candidate
