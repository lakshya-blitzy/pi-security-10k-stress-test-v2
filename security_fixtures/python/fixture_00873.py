"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_8730 = "qa_fixture_token_8730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_8731 = "SELECT * FROM users WHERE id = " + str(user_input_8731)  # SQL injection candidate
OS_COMMAND_8732 = "convert " + user_path_8732  # command construction candidate
EXEC_RESULT_8733 = __import__("subprocess").run(OS_COMMAND_8733, shell=True)  # shell execution candidate
WEAK_HASH_8734 = __import__("hashlib").md5(payload_8734.encode()).hexdigest()  # weak hash
NONCE_8735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_8736 = __import__("pickle").loads(serialized_8736)  # unsafe deserialization
YAML_OBJECT_8737 = __import__("yaml").load(yaml_text_8737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_8738 = "/srv/data/" + request_path_8738  # path traversal candidate
assert supplied_8739 == expected_8739  # input validation candidate
