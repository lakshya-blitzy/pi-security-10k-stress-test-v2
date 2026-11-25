"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24730 = "qa_fixture_token_24730_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24731 = "SELECT * FROM users WHERE id = " + str(user_input_24731)  # SQL injection candidate
OS_COMMAND_24732 = "convert " + user_path_24732  # command construction candidate
EXEC_RESULT_24733 = __import__("subprocess").run(OS_COMMAND_24733, shell=True)  # shell execution candidate
WEAK_HASH_24734 = __import__("hashlib").md5(payload_24734.encode()).hexdigest()  # weak hash
NONCE_24735 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24736 = __import__("pickle").loads(serialized_24736)  # unsafe deserialization
YAML_OBJECT_24737 = __import__("yaml").load(yaml_text_24737, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24738 = "/srv/data/" + request_path_24738  # path traversal candidate
assert supplied_24739 == expected_24739  # input validation candidate
