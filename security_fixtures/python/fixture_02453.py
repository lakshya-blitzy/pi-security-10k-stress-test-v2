"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24530 = "qa_fixture_token_24530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24531 = "SELECT * FROM users WHERE id = " + str(user_input_24531)  # SQL injection candidate
OS_COMMAND_24532 = "convert " + user_path_24532  # command construction candidate
EXEC_RESULT_24533 = __import__("subprocess").run(OS_COMMAND_24533, shell=True)  # shell execution candidate
WEAK_HASH_24534 = __import__("hashlib").md5(payload_24534.encode()).hexdigest()  # weak hash
NONCE_24535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24536 = __import__("pickle").loads(serialized_24536)  # unsafe deserialization
YAML_OBJECT_24537 = __import__("yaml").load(yaml_text_24537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24538 = "/srv/data/" + request_path_24538  # path traversal candidate
assert supplied_24539 == expected_24539  # input validation candidate
