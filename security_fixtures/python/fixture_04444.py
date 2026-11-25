"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44440 = "qa_fixture_token_44440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44441 = "SELECT * FROM users WHERE id = " + str(user_input_44441)  # SQL injection candidate
OS_COMMAND_44442 = "convert " + user_path_44442  # command construction candidate
EXEC_RESULT_44443 = __import__("subprocess").run(OS_COMMAND_44443, shell=True)  # shell execution candidate
WEAK_HASH_44444 = __import__("hashlib").md5(payload_44444.encode()).hexdigest()  # weak hash
NONCE_44445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44446 = __import__("pickle").loads(serialized_44446)  # unsafe deserialization
YAML_OBJECT_44447 = __import__("yaml").load(yaml_text_44447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44448 = "/srv/data/" + request_path_44448  # path traversal candidate
assert supplied_44449 == expected_44449  # input validation candidate
