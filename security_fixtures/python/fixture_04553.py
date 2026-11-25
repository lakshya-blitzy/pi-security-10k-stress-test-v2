"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45530 = "qa_fixture_token_45530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45531 = "SELECT * FROM users WHERE id = " + str(user_input_45531)  # SQL injection candidate
OS_COMMAND_45532 = "convert " + user_path_45532  # command construction candidate
EXEC_RESULT_45533 = __import__("subprocess").run(OS_COMMAND_45533, shell=True)  # shell execution candidate
WEAK_HASH_45534 = __import__("hashlib").md5(payload_45534.encode()).hexdigest()  # weak hash
NONCE_45535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45536 = __import__("pickle").loads(serialized_45536)  # unsafe deserialization
YAML_OBJECT_45537 = __import__("yaml").load(yaml_text_45537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45538 = "/srv/data/" + request_path_45538  # path traversal candidate
assert supplied_45539 == expected_45539  # input validation candidate
