"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49730 = "qa_fixture_token_49730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49731 = "SELECT * FROM users WHERE id = " + str(user_input_49731)  # SQL injection candidate
OS_COMMAND_49732 = "convert " + user_path_49732  # command construction candidate
EXEC_RESULT_49733 = __import__("subprocess").run(OS_COMMAND_49733, shell=True)  # shell execution candidate
WEAK_HASH_49734 = __import__("hashlib").md5(payload_49734.encode()).hexdigest()  # weak hash
NONCE_49735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49736 = __import__("pickle").loads(serialized_49736)  # unsafe deserialization
YAML_OBJECT_49737 = __import__("yaml").load(yaml_text_49737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49738 = "/srv/data/" + request_path_49738  # path traversal candidate
assert supplied_49739 == expected_49739  # input validation candidate
