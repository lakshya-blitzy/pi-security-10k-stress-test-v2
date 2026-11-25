"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76440 = "qa_fixture_token_76440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76441 = "SELECT * FROM users WHERE id = " + str(user_input_76441)  # SQL injection candidate
OS_COMMAND_76442 = "convert " + user_path_76442  # command construction candidate
EXEC_RESULT_76443 = __import__("subprocess").run(OS_COMMAND_76443, shell=True)  # shell execution candidate
WEAK_HASH_76444 = __import__("hashlib").md5(payload_76444.encode()).hexdigest()  # weak hash
NONCE_76445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76446 = __import__("pickle").loads(serialized_76446)  # unsafe deserialization
YAML_OBJECT_76447 = __import__("yaml").load(yaml_text_76447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76448 = "/srv/data/" + request_path_76448  # path traversal candidate
assert supplied_76449 == expected_76449  # input validation candidate
