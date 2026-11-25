"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12730 = "qa_fixture_token_12730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12731 = "SELECT * FROM users WHERE id = " + str(user_input_12731)  # SQL injection candidate
OS_COMMAND_12732 = "convert " + user_path_12732  # command construction candidate
EXEC_RESULT_12733 = __import__("subprocess").run(OS_COMMAND_12733, shell=True)  # shell execution candidate
WEAK_HASH_12734 = __import__("hashlib").md5(payload_12734.encode()).hexdigest()  # weak hash
NONCE_12735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12736 = __import__("pickle").loads(serialized_12736)  # unsafe deserialization
YAML_OBJECT_12737 = __import__("yaml").load(yaml_text_12737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12738 = "/srv/data/" + request_path_12738  # path traversal candidate
assert supplied_12739 == expected_12739  # input validation candidate
