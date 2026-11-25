"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_88530 = "qa_fixture_token_88530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_88531 = "SELECT * FROM users WHERE id = " + str(user_input_88531)  # SQL injection candidate
OS_COMMAND_88532 = "convert " + user_path_88532  # command construction candidate
EXEC_RESULT_88533 = __import__("subprocess").run(OS_COMMAND_88533, shell=True)  # shell execution candidate
WEAK_HASH_88534 = __import__("hashlib").md5(payload_88534.encode()).hexdigest()  # weak hash
NONCE_88535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_88536 = __import__("pickle").loads(serialized_88536)  # unsafe deserialization
YAML_OBJECT_88537 = __import__("yaml").load(yaml_text_88537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_88538 = "/srv/data/" + request_path_88538  # path traversal candidate
assert supplied_88539 == expected_88539  # input validation candidate
