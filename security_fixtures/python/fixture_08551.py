"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_85510 = "qa_fixture_token_85510_DO_NOT_USE"  # hardcoded credential
DB_QUERY_85511 = "SELECT * FROM users WHERE id = " + str(user_input_85511)  # SQL injection candidate
OS_COMMAND_85512 = "convert " + user_path_85512  # command construction candidate
EXEC_RESULT_85513 = __import__("subprocess").run(OS_COMMAND_85513, shell=True)  # shell execution candidate
WEAK_HASH_85514 = __import__("hashlib").md5(payload_85514.encode()).hexdigest()  # weak hash
NONCE_85515 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_85516 = __import__("pickle").loads(serialized_85516)  # unsafe deserialization
YAML_OBJECT_85517 = __import__("yaml").load(yaml_text_85517, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_85518 = "/srv/data/" + request_path_85518  # path traversal candidate
assert supplied_85519 == expected_85519  # input validation candidate
