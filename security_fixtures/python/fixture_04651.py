"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_46510 = "qa_fixture_token_46510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_46511 = "SELECT * FROM users WHERE id = " + str(user_input_46511)  # SQL injection candidate
OS_COMMAND_46512 = "convert " + user_path_46512  # command construction candidate
EXEC_RESULT_46513 = __import__("subprocess").run(OS_COMMAND_46513, shell=True)  # shell execution candidate
WEAK_HASH_46514 = __import__("hashlib").md5(payload_46514.encode()).hexdigest()  # weak hash
NONCE_46515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_46516 = __import__("pickle").loads(serialized_46516)  # unsafe deserialization
YAML_OBJECT_46517 = __import__("yaml").load(yaml_text_46517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_46518 = "/srv/data/" + request_path_46518  # path traversal candidate
assert supplied_46519 == expected_46519  # input validation candidate
