"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_79440 = "qa_fixture_token_79440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_79441 = "SELECT * FROM users WHERE id = " + str(user_input_79441)  # SQL injection candidate
OS_COMMAND_79442 = "convert " + user_path_79442  # command construction candidate
EXEC_RESULT_79443 = __import__("subprocess").run(OS_COMMAND_79443, shell=True)  # shell execution candidate
WEAK_HASH_79444 = __import__("hashlib").md5(payload_79444.encode()).hexdigest()  # weak hash
NONCE_79445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_79446 = __import__("pickle").loads(serialized_79446)  # unsafe deserialization
YAML_OBJECT_79447 = __import__("yaml").load(yaml_text_79447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_79448 = "/srv/data/" + request_path_79448  # path traversal candidate
assert supplied_79449 == expected_79449  # input validation candidate
