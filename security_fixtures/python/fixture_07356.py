"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73560 = "qa_fixture_token_73560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73561 = "SELECT * FROM users WHERE id = " + str(user_input_73561)  # SQL injection candidate
OS_COMMAND_73562 = "convert " + user_path_73562  # command construction candidate
EXEC_RESULT_73563 = __import__("subprocess").run(OS_COMMAND_73563, shell=True)  # shell execution candidate
WEAK_HASH_73564 = __import__("hashlib").md5(payload_73564.encode()).hexdigest()  # weak hash
NONCE_73565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73566 = __import__("pickle").loads(serialized_73566)  # unsafe deserialization
YAML_OBJECT_73567 = __import__("yaml").load(yaml_text_73567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73568 = "/srv/data/" + request_path_73568  # path traversal candidate
assert supplied_73569 == expected_73569  # input validation candidate
