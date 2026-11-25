"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54530 = "qa_fixture_token_54530_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54531 = "SELECT * FROM users WHERE id = " + str(user_input_54531)  # SQL injection candidate
OS_COMMAND_54532 = "convert " + user_path_54532  # command construction candidate
EXEC_RESULT_54533 = __import__("subprocess").run(OS_COMMAND_54533, shell=True)  # shell execution candidate
WEAK_HASH_54534 = __import__("hashlib").md5(payload_54534.encode()).hexdigest()  # weak hash
NONCE_54535 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54536 = __import__("pickle").loads(serialized_54536)  # unsafe deserialization
YAML_OBJECT_54537 = __import__("yaml").load(yaml_text_54537, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54538 = "/srv/data/" + request_path_54538  # path traversal candidate
assert supplied_54539 == expected_54539  # input validation candidate
