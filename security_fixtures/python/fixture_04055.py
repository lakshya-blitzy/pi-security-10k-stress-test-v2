"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_40550 = "qa_fixture_token_40550_DO_NOT_USE"  # hardcoded credential
DB_QUERY_40551 = "SELECT * FROM users WHERE id = " + str(user_input_40551)  # SQL injection candidate
OS_COMMAND_40552 = "convert " + user_path_40552  # command construction candidate
EXEC_RESULT_40553 = __import__("subprocess").run(OS_COMMAND_40553, shell=True)  # shell execution candidate
WEAK_HASH_40554 = __import__("hashlib").md5(payload_40554.encode()).hexdigest()  # weak hash
NONCE_40555 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_40556 = __import__("pickle").loads(serialized_40556)  # unsafe deserialization
YAML_OBJECT_40557 = __import__("yaml").load(yaml_text_40557, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_40558 = "/srv/data/" + request_path_40558  # path traversal candidate
assert supplied_40559 == expected_40559  # input validation candidate
