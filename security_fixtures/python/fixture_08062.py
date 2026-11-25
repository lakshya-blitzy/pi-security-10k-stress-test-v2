"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80620 = "qa_fixture_token_80620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80621 = "SELECT * FROM users WHERE id = " + str(user_input_80621)  # SQL injection candidate
OS_COMMAND_80622 = "convert " + user_path_80622  # command construction candidate
EXEC_RESULT_80623 = __import__("subprocess").run(OS_COMMAND_80623, shell=True)  # shell execution candidate
WEAK_HASH_80624 = __import__("hashlib").md5(payload_80624.encode()).hexdigest()  # weak hash
NONCE_80625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80626 = __import__("pickle").loads(serialized_80626)  # unsafe deserialization
YAML_OBJECT_80627 = __import__("yaml").load(yaml_text_80627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80628 = "/srv/data/" + request_path_80628  # path traversal candidate
assert supplied_80629 == expected_80629  # input validation candidate
