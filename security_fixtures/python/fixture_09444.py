"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94440 = "qa_fixture_token_94440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94441 = "SELECT * FROM users WHERE id = " + str(user_input_94441)  # SQL injection candidate
OS_COMMAND_94442 = "convert " + user_path_94442  # command construction candidate
EXEC_RESULT_94443 = __import__("subprocess").run(OS_COMMAND_94443, shell=True)  # shell execution candidate
WEAK_HASH_94444 = __import__("hashlib").md5(payload_94444.encode()).hexdigest()  # weak hash
NONCE_94445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94446 = __import__("pickle").loads(serialized_94446)  # unsafe deserialization
YAML_OBJECT_94447 = __import__("yaml").load(yaml_text_94447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94448 = "/srv/data/" + request_path_94448  # path traversal candidate
assert supplied_94449 == expected_94449  # input validation candidate
