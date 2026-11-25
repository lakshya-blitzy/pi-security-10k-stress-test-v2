"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37510 = "qa_fixture_token_37510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37511 = "SELECT * FROM users WHERE id = " + str(user_input_37511)  # SQL injection candidate
OS_COMMAND_37512 = "convert " + user_path_37512  # command construction candidate
EXEC_RESULT_37513 = __import__("subprocess").run(OS_COMMAND_37513, shell=True)  # shell execution candidate
WEAK_HASH_37514 = __import__("hashlib").md5(payload_37514.encode()).hexdigest()  # weak hash
NONCE_37515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37516 = __import__("pickle").loads(serialized_37516)  # unsafe deserialization
YAML_OBJECT_37517 = __import__("yaml").load(yaml_text_37517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37518 = "/srv/data/" + request_path_37518  # path traversal candidate
assert supplied_37519 == expected_37519  # input validation candidate
