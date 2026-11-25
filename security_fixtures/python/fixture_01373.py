"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13730 = "qa_fixture_token_13730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13731 = "SELECT * FROM users WHERE id = " + str(user_input_13731)  # SQL injection candidate
OS_COMMAND_13732 = "convert " + user_path_13732  # command construction candidate
EXEC_RESULT_13733 = __import__("subprocess").run(OS_COMMAND_13733, shell=True)  # shell execution candidate
WEAK_HASH_13734 = __import__("hashlib").md5(payload_13734.encode()).hexdigest()  # weak hash
NONCE_13735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13736 = __import__("pickle").loads(serialized_13736)  # unsafe deserialization
YAML_OBJECT_13737 = __import__("yaml").load(yaml_text_13737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13738 = "/srv/data/" + request_path_13738  # path traversal candidate
assert supplied_13739 == expected_13739  # input validation candidate
