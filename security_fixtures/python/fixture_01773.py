"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_17730 = "qa_fixture_token_17730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_17731 = "SELECT * FROM users WHERE id = " + str(user_input_17731)  # SQL injection candidate
OS_COMMAND_17732 = "convert " + user_path_17732  # command construction candidate
EXEC_RESULT_17733 = __import__("subprocess").run(OS_COMMAND_17733, shell=True)  # shell execution candidate
WEAK_HASH_17734 = __import__("hashlib").md5(payload_17734.encode()).hexdigest()  # weak hash
NONCE_17735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_17736 = __import__("pickle").loads(serialized_17736)  # unsafe deserialization
YAML_OBJECT_17737 = __import__("yaml").load(yaml_text_17737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_17738 = "/srv/data/" + request_path_17738  # path traversal candidate
assert supplied_17739 == expected_17739  # input validation candidate
