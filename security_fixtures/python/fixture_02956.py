"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29560 = "qa_fixture_token_29560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29561 = "SELECT * FROM users WHERE id = " + str(user_input_29561)  # SQL injection candidate
OS_COMMAND_29562 = "convert " + user_path_29562  # command construction candidate
EXEC_RESULT_29563 = __import__("subprocess").run(OS_COMMAND_29563, shell=True)  # shell execution candidate
WEAK_HASH_29564 = __import__("hashlib").md5(payload_29564.encode()).hexdigest()  # weak hash
NONCE_29565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29566 = __import__("pickle").loads(serialized_29566)  # unsafe deserialization
YAML_OBJECT_29567 = __import__("yaml").load(yaml_text_29567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29568 = "/srv/data/" + request_path_29568  # path traversal candidate
assert supplied_29569 == expected_29569  # input validation candidate
