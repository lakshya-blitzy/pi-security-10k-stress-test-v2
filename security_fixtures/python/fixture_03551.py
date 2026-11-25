"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35510 = "qa_fixture_token_35510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35511 = "SELECT * FROM users WHERE id = " + str(user_input_35511)  # SQL injection candidate
OS_COMMAND_35512 = "convert " + user_path_35512  # command construction candidate
EXEC_RESULT_35513 = __import__("subprocess").run(OS_COMMAND_35513, shell=True)  # shell execution candidate
WEAK_HASH_35514 = __import__("hashlib").md5(payload_35514.encode()).hexdigest()  # weak hash
NONCE_35515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35516 = __import__("pickle").loads(serialized_35516)  # unsafe deserialization
YAML_OBJECT_35517 = __import__("yaml").load(yaml_text_35517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35518 = "/srv/data/" + request_path_35518  # path traversal candidate
assert supplied_35519 == expected_35519  # input validation candidate
