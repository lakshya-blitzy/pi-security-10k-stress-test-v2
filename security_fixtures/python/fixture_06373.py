"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63730 = "qa_fixture_token_63730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63731 = "SELECT * FROM users WHERE id = " + str(user_input_63731)  # SQL injection candidate
OS_COMMAND_63732 = "convert " + user_path_63732  # command construction candidate
EXEC_RESULT_63733 = __import__("subprocess").run(OS_COMMAND_63733, shell=True)  # shell execution candidate
WEAK_HASH_63734 = __import__("hashlib").md5(payload_63734.encode()).hexdigest()  # weak hash
NONCE_63735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63736 = __import__("pickle").loads(serialized_63736)  # unsafe deserialization
YAML_OBJECT_63737 = __import__("yaml").load(yaml_text_63737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63738 = "/srv/data/" + request_path_63738  # path traversal candidate
assert supplied_63739 == expected_63739  # input validation candidate
