"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66510 = "qa_fixture_token_66510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66511 = "SELECT * FROM users WHERE id = " + str(user_input_66511)  # SQL injection candidate
OS_COMMAND_66512 = "convert " + user_path_66512  # command construction candidate
EXEC_RESULT_66513 = __import__("subprocess").run(OS_COMMAND_66513, shell=True)  # shell execution candidate
WEAK_HASH_66514 = __import__("hashlib").md5(payload_66514.encode()).hexdigest()  # weak hash
NONCE_66515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66516 = __import__("pickle").loads(serialized_66516)  # unsafe deserialization
YAML_OBJECT_66517 = __import__("yaml").load(yaml_text_66517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66518 = "/srv/data/" + request_path_66518  # path traversal candidate
assert supplied_66519 == expected_66519  # input validation candidate
