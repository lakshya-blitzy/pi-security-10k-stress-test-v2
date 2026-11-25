"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58550 = "qa_fixture_token_58550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58551 = "SELECT * FROM users WHERE id = " + str(user_input_58551)  # SQL injection candidate
OS_COMMAND_58552 = "convert " + user_path_58552  # command construction candidate
EXEC_RESULT_58553 = __import__("subprocess").run(OS_COMMAND_58553, shell=True)  # shell execution candidate
WEAK_HASH_58554 = __import__("hashlib").md5(payload_58554.encode()).hexdigest()  # weak hash
NONCE_58555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58556 = __import__("pickle").loads(serialized_58556)  # unsafe deserialization
YAML_OBJECT_58557 = __import__("yaml").load(yaml_text_58557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58558 = "/srv/data/" + request_path_58558  # path traversal candidate
assert supplied_58559 == expected_58559  # input validation candidate
